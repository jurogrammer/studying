# In public classes, use accessor methods, not public fields

```java
// Degenerate classes like this should not be public!
class Point {
  public double x;
  public double y;
}
```

### 위 코드 문제점

직접적으로 필드에 접근하기 때문에 encapsulation 장점을 못누림

1. API를 변경하기 않고는 변경불가
2. 불변 값을 강제 못함
3. 값이 사용될 때 보조액션을 취할 수 없게 됨

따라서 object oriented programmers들은 이를 *accessor methods*(getters) and *mutators*(setters)를 이용하여 바꿔야한다고 생각합니다. 아래처럼 말이죠

### Getter Setter

```java
// Encapsulation of data by accessor methods and mutators
class Point {
  private double x;
  private double y;
  public Point(double x, double y) {
    this.x = x;
    this.y = y; 
  }
  //accessor method, mutator
  public double getX() { return x; }
  public double getY() { return y; }
  public void setX(double x) { this.x = x; }
  public void setY(double y) { this.y = y; }
}
```

이는 public class라면 옳습니다만, 클래스가 package-private 이거나 priate nested class라면 노출시켜도 문제 없습니다.

적절히 노출시켜준다면 이 클라이언트의 method에 accessor method로 접근하는 것보다 난잡하지 않습니다. 이 클래스를 사용하는 client의 코드 면에서나, class의 구현 면 두 부분에서 말이죠.



### Java library에서 이 룰은 어긴 예 - java.awt package

모방의 예로 보면 안되고 피해야할 예로 보면 되겠습니다. 이 패키지에서 Dimesion을 외부에서 사용할 경우 심각한 성능 저하 문제를 초래하기 때문이지요. 이는 지금까지도 문제가 되고 있습니다.



### public으로 선언해도 조금만 문제되는 예

한편으로 public으로 덜 문제가 되는 예가 있습니다. 바로 immutable fields에서 말이죠.

비록, API를 변경하지 않고서는 representation을 변경할 수 없고, 보조 액션을 취할 순 없으나 invariant는 적용할 수 있습니다.

```java
// Public class with exposed immutable fields - questionable
public final class Time {
  private static final int HOURS_PER_DAY    = 24;
  private static final int MINUTES_PER_HOUR = 60;
  public final int hour;
  public final int minute;
  public Time(int hour, int minute) {
    if (hour < 0 || hour >= HOURS_PER_DAY)
      throw new IllegalArgumentException("Hour: " + hour);
    if (minute < 0 || minute >= MINUTES_PER_HOUR)
      throw new IllegalArgumentException("Min: " + minute);
    this.hour = hour;
    this.minute = minute;
	}
       ... // Remainder omitted
}

```

