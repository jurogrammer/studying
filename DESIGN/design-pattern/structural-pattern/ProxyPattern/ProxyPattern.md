# 참고자료

* https://refactoring.guru/design-patterns/proxy

* https://en.wikipedia.org/wiki/Proxy_pattern

* proxy : 대리인, 대용물



# ProxyPattern이란?

* structual design-pattern
* 실제 서비스에 대해 대리인을 둠으로써  **클라이언트가 실제 서비스 접근**하는 것을 **대리인이 컨트롤**할 수 있는 패턴입니다.





# 상황 - 언제 실 서비스 접근에 대한 컨트롤이 필요할까?

<img src="https://refactoring.guru/images/patterns/diagrams/proxy/problem-en-2x.png" style="zoom: 67%;" />

* DB에 접속하여 서비스의 많은 리소스를 잡아먹을 수 있는 object가 있습니다.
* 이 object는 때때로 실행됩니다.



이를 위해 lazy initialization을 생각해볼 수 있습니다. 

다시 말해서 필요한 순간에 object를 생성하여 DB에 접근하도록 컨트롤하고 싶은 상황입니다.



### 안 좋은 접근

1. object를 사용하는 client 코드들을 lazy initialization으로 수정

   * client 하나하나 수정해야하기 때문에 코드 중복이 발생할 수 있습니다.

2. object 자체를 lazy initialization으로 수정

   * object가 3rd-party library일 경우 수정할 수가 없습니다.

   

# 해결책 - 대리인을 두어라!

<img src="https://refactoring.guru/images/patterns/diagrams/proxy/solution-en-2x.png" style="zoom:50%;" />

1. 위 그림처럼 database와 interface가 동일한 proxy class를 앞에 둡니다.

2. 그리고 클라이언트가 database가 아닌, proxy에 대해 요청을 하도록 합니다.
3. 클라이언트가 요청시 proxy에서 object를 초기화하여 실 서비스에 대해 로직을 수행하도록 합니다.



# 구조

<img src="https://refactoring.guru/images/patterns/diagrams/proxy/structure-indexed-2x.png" style="zoom:50%;" />

### 1. ServiceInterface

Proxy와 Service가 동일한 인터페이스를 가지도록 하기 위해 Service의 인터페이스를 생성합니다.

### 2. Service

서비스는 실제 비즈니스의 로직이 있는 부분입니다.

### 3.Proxy

프록시는 service에 대해 reference field를 지니고 있습니다. 작업을 위임하고, 컨트롤하기 위해서 이지요.



### 4. Client

클라이언트는 Proxy를 실 서비스처럼 사용합니다.





# 사용 예

1. lazy initialization
2. 보안
   * 실서비스 접근 시 proxy가 사용자 권한을 확인하여 접근을 허용할 지, 거부할 지 판단
3. 로깅
4. 캐싱



# 예시 - 유튜브 캐싱 라이브러리



<img src="https://refactoring.guru/images/patterns/diagrams/proxy/example-2x.png" style="zoom:50%;" />

### 1. ThirdParty YouTubeLib

```java
public interface ThirdPartyYouTubeLib {
    HashMap<String, Video> popularVideos();

    Video getVideo(String videoId);
}
```

### 2.ThirdPartyYouTubeClass

```java
public class ThirdPartyYouTubeClass implements ThirdPartyYouTubeLib {

    @Override
    public HashMap<String, Video> popularVideos() {
        connectToServer("http://www.youtube.com");
        return getRandomVideos();
    }

    @Override
    public Video getVideo(String videoId) {
        connectToServer("http://www.youtube.com/" + videoId);
        return getSomeVideo(videoId);
    }

    // -----------------------------------------------------------------------
    // Fake methods to simulate network activity. They as slow as a real life.

    private int random(int min, int max) {
        return min + (int) (Math.random() * ((max - min) + 1));
    }

    private void experienceNetworkLatency() {
        int randomLatency = random(5, 10);
        for (int i = 0; i < randomLatency; i++) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        }
    }

    private void connectToServer(String server) {
        System.out.print("Connecting to " + server + "... ");
        experienceNetworkLatency();
        System.out.print("Connected!" + "\n");
    }

    private HashMap<String, Video> getRandomVideos() {
        System.out.print("Downloading populars... ");

        experienceNetworkLatency();
        HashMap<String, Video> hmap = new HashMap<String, Video>();
        hmap.put("catzzzzzzzzz", new Video("sadgahasgdas", "Catzzzz.avi"));
        hmap.put("mkafksangasj", new Video("mkafksangasj", "Dog play with ball.mp4"));
        hmap.put("dancesvideoo", new Video("asdfas3ffasd", "Dancing video.mpq"));
        hmap.put("dlsdk5jfslaf", new Video("dlsdk5jfslaf", "Barcelona vs RealM.mov"));
        hmap.put("3sdfgsd1j333", new Video("3sdfgsd1j333", "Programing lesson#1.avi"));

        System.out.print("Done!" + "\n");
        return hmap;
    }

    private Video getSomeVideo(String videoId) {
        System.out.print("Downloading video... ");

        experienceNetworkLatency();
        Video video = new Video(videoId, "Some video title");

        System.out.print("Done!" + "\n");
        return video;
    }

}
```



### 3. Video

```java
public class Video {
    public String id;
    public String title;
    public String data;

    Video(String id, String title) {
        this.id = id;
        this.title = title;
        this.data = "Random video.";
    }
}
```



### 4. caching Proxy

```java
public class YouTubeCacheProxy implements ThirdPartyYouTubeLib {
    private ThirdPartyYouTubeLib youtubeService;
    private HashMap<String, Video> cachePopular = new HashMap<String, Video>();
    private HashMap<String, Video> cacheAll = new HashMap<String, Video>();

    public YouTubeCacheProxy() {
        this.youtubeService = new ThirdPartyYouTubeClass();
    }

    @Override
    public HashMap<String, Video> popularVideos() {
        if (cachePopular.isEmpty()) {
            cachePopular = youtubeService.popularVideos();
        } else {
            System.out.println("Retrieved list from cache.");
        }
        return cachePopular;
    }

    @Override
    public Video getVideo(String videoId) {
        Video video = cacheAll.get(videoId);
        if (video == null) {
            video = youtubeService.getVideo(videoId);
            cacheAll.put(videoId, video);
        } else {
            System.out.println("Retrieved video '" + videoId + "' from cache.");
        }
        return video;
    }

    public void reset() {
        cachePopular.clear();
        cacheAll.clear();
    }
}
```





### 4. YouTubeDownloader

```java
public class YouTubeDownloader {
    private ThirdPartyYouTubeLib api;

    public YouTubeDownloader(ThirdPartyYouTubeLib api) {
        this.api = api;
    }

    public void renderVideoPage(String videoId) {
        Video video = api.getVideo(videoId);
        System.out.println("\n-------------------------------");
        System.out.println("Video page (imagine fancy HTML)");
        System.out.println("ID: " + video.id);
        System.out.println("Title: " + video.title);
        System.out.println("Video: " + video.data);
        System.out.println("-------------------------------\n");
    }

    public void renderPopularVideos() {
        HashMap<String, Video> list = api.popularVideos();
        System.out.println("\n-------------------------------");
        System.out.println("Most popular videos on YouTube (imagine fancy HTML)");
        for (Video video : list.values()) {
            System.out.println("ID: " + video.id + " / Title: " + video.title);
        }
        System.out.println("-------------------------------\n");
    }
}
```



### 5. Demo

```java
public class Demo {

    public static void main(String[] args) {
        YouTubeDownloader naiveDownloader = new YouTubeDownloader(new ThirdPartyYouTubeClass());
        YouTubeDownloader smartDownloader = new YouTubeDownloader(new YouTubeCacheProxy());

        long naive = test(naiveDownloader);
        long smart = test(smartDownloader);
        System.out.print("Time saved by caching proxy: " + (naive - smart) + "ms");

    }

    private static long test(YouTubeDownloader downloader) {
        long startTime = System.currentTimeMillis();

        // User behavior in our app:
        downloader.renderPopularVideos();
        downloader.renderVideoPage("catzzzzzzzzz");
        downloader.renderPopularVideos();
        downloader.renderVideoPage("dancesvideoo");
        // Users might visit the same page quite often.
        downloader.renderVideoPage("catzzzzzzzzz");
        downloader.renderVideoPage("someothervid");

        long estimatedTime = System.currentTimeMillis() - startTime;
        System.out.print("Time elapsed: " + estimatedTime + "ms\n");
        return estimatedTime;
    }
}
```





### 마무리

The proxy could interface to anything: a network connection, a large object in memory, a file, or some other resource that is expensive or impossible to duplicate. 

In short, a proxy is a wrapper or agent object that is being called by the client to access the real serving object behind the scenes.



---

디자인 패턴을 10개 넘게 소개하면서 눈에 띄는 객체관계가 있습니다. 바로 aggregation, composition입니다. 결국 이 패턴을 쓰는 이유는 2가지로  볼 수 있습니다.

1. 작업을 위임할 수 있다.
2. 서비스를 곧 바로 실행하는 것이 아닌, 해당 object를 통해 실 작업을 실행하기 때문에 해당 Object에 대한 로직을 넣을 수 있습니다.