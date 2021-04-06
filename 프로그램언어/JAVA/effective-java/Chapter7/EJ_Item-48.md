# Item 48 Use caution when making streams parallel

Java는 parallel 측면에서 발빠르게 기능을 지원해주었고, parallel method가 등장하기 이르렀습니다. stream에서 .parallel()만 작성해준다면 병렬처리가 가능해지죠.



하지만, 쉽게 작성할 수 있다하여 올바르게 작성하는 일이 쉬워진 건 아니죠. parallel programming할 땐 safety, liveness상태를 유지하기 위해 애써야 합니다.



예제를 통해서 알아보죠.



## Mersene primes

### 코드

```java
// Stream-based program to generate the first 20 Mersenne primes
public static void main(String[] args) {
  primes()
    .parallel()
    .map(p -> TWO.pow(p.intValueExact()).subtract(ONE))
    .filter(mersenne -> mersenne.isProbablePrime(50))
    .limit(20)
    .forEach(System.out::println);
}
static Stream<BigInteger> primes() {
  return Stream.iterate(TWO, BigInteger::nextProbablePrime);
}
```

> 참고로 TWO는 java8에선 private static class라 호출할 수 없습니다.

싱글 스레드로 처리할 경우 즉각 소수를 찍기 시작해서 프로세스가 금방 종료됩니다. 하지만, `parallel()` 를 추가한 위 코드를 실행항하면 어떻게 될까요?

### 결과

1. 싱글에선 즉각 출력되었던 것에 비해, 아무것도 출력되지 않습니다.
2. 그리고 cpu를 90%이상 차지하게 되죠.



### 원인

스트림 라이브러리가 해당 파이프라인을 병렬화하는 방법을 찾아내지 못했기 때문입니다.

* data source가 iterate일 경우,

* 그리고 limit을 중간 연산으로 쓸 경우

parallel의 효과를 취할 수 없습니다.



#### Limit의 문제점

쓰레드가 남아있으면 일단 할당하고 보는 알고리즘이 문제가 됩니다.

만약에 sequence element가 있고, 코어의 쓰레드가 5개가 남고, limit이 1개가 걸려있다고 봅시다.

limit이 1개여도 쓰레드가 4개가 남았기 때문에 4개의 elements를 더 할당하여 처리합니다.

실제 처리할 1개의 elements가 먼저 끝났다 하더라도 나머지 4개의 쓰레드는 처리하고 있는 상태가 됩니다.

### 테스트

#### limit

![스크린샷 2021-03-15 오후 8.39.36](/Users/ju/Library/Application Support/typora-user-images/스크린샷 2021-03-15 오후 8.39.36.png)



#### iterate + limit

![스크린샷 2021-03-15 오후 8.40.20](/Users/ju/Library/Application Support/typora-user-images/스크린샷 2021-03-15 오후 8.40.20.png)

잉; 이건 잘 작동하네요...

아마 메르센 소수 계산이 엄청 오래 걸려서 그런 것 같습니다?...? 그렇다고 보기엔 어떤 값도 출력되지 않아서 이상하네요.



## 병렬화 효과가 좋은 경우

### 1. Stream source

병렬화 효과가 좋은 data source는 따로 있습니다.

* ArrayList
* HashMap
* HashSet
* ConcurrentHashMap
* array
* int ranges
* long ranges



### 이유

#### 1) 다수의 스레드에 분배하기 좋은 형태

데이터를 원하는 크기로 손쉽게 자를 수 있기 때문이죠.

나누는 작업은 Spliterator가 담당합니다.

#### 2) locality of reference가 뛰어납니다.

이웃한 원소들이 연속적으로 나열되어 있기 때문에 cpu cache hit ratio가 올라가죠.

#### 

### 2. Terminal operation

종단 연산에 따라 병렬화 속도가 달라지죠.



우선, sequential연산은 병렬화 속도가 상당히 제한되겠죠?

terminal연산 중 가장 병렬화에 적합한 연산은 Reduction연산입니다.

* sum
* max
* count
* sum

같은 연산 그리고, 맞으면 바로 종료되는

* anyMatch
* allMatch
* noneMatch

가 사용하기 좋죠.

한편으로는 collect 메서드는 mutable reduction을 수행하는데, 최종적으로 합칠 때 부담이 커 적합하지 않습니다.



### 3. 직접 구현시

직접 구현한 Stream, Iterable, Collection의 병렬화 이점을 누리고 싶다면 spliterator method를 반드시 overriding 후, 강도 높게 테스트 진행해야 합니다. 자세한 방법은 난이도가 높아 이 책에선 다루지 않습니다.



## 병렬화 적용할 시 고려해야할 사항

### safety failure

잘못 병렬화하여 결과자체가 잘못되거나 에상 못한 동작이 발생한 경우를 safety failure라고 부릅니다. 이러한 문제 때문에 Stream명세는 엄중한 규약을 명시하죠



### 예시

Stream의 reduce연산에는 accumulator, combiner함수는 다음 조건을 만족해야 합니다.

1. associative(결합법칙)
2. non-interfering
3. stateless

위를 준수하지 않았을 때 safety failure가 발생하죠.



> 출력 순서가 올바르지 않은 경우도 이에 해당하는데 이때는 forEach대신 forEachOrdered를 사용하시면 됩니다.



### 병렬화로 인한 오버헤드

병렬화 구성을 위해 리소스를 또 사용하기 마련입니다. 추정해보는 간단한 공식이 있습니다.

`squence elements의 수 x elements별 수행되는 코드의 줄 수 > 수십만`

위 경우에만 병렬화로 인한 오버헤드보다 병렬화 이점이 더 크기 때문이죠.



### 다른 시스템 영향

공통의 fork-join pool(동일 풀)을 공유하기 때문에 다른 서비스에 영향을 미칠 수 있습니다. 따라서 테스트할 때는 배포 환경과 동일한 환경에서 테스트해보시길 바랍니다.



이 문제들을 다 읽다보면, 도대체 언제 parallel을 사용해야하나 싶죠? 맞습니다... 거의 쓸 상황이 없어요. 정말 필요한 경우에만 사용하시길 바랍니다. 다음은 그 예를 보여드리도록 하겠습니다.



## parallel을 잘 사용한 케이스

π(n)을 구하는 예제입니다. 

> π(n)이란, n보다 작거나 같은 소수의 개수를 반환하는 함수입니다.



### 일반 버전

```java
// Prime-counting stream pipeline - benefits from parallelization
static long pi(long n) {
  return LongStream.rangeClosed(2, n)
    .mapToObj(BigInteger::valueOf)
    .filter(i -> i.isProbablePrime(50))
    .count();
}
```



### parallel버전

```java
// Prime-counting stream pipeline - benefits from parallelization
static long pi(long n) {
  return LongStream.rangeClosed(2, n)
    .parallel()
    .mapToObj(BigInteger::valueOf)
    .filter(i -> i.isProbablePrime(50))
    .count();
}
```

단지 parallel하나 들어간 것만으로도 4코어 processor에선 3.37배가 빨라졌습니다.



### Random numbers Parallel

무작위 수에 대해 병렬 수행할 경우에는 ThreadLocalRandom보다는 SplittableRandom을 사용하세요.

parallel에 대응하기 위해 만들어진 메서드이기 때문에 코어의 수에 선형적으로 비례해서 속도가 증가합니다. 그에 반면 ThreadLocalRandom은 싱글 쓰레드에서 사용하기 위해 만들어졌기 때문에 성능에 제한이 있죠.

Random 모든 연산을 동기화해서 병렬처리엔 최악입니다.