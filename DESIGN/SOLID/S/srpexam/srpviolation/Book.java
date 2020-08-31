package srpexam.srpviolation;

/*
* Book클래스를 소비하는 행위자가 사서와 프린트기(printCurrentPage) 두 개가 될 수 있음
* 따라서 책임의 원인을 두 개로 가지고 있으므로 이를 분리 할 것.
* */
public class Book {
    private String title;
    private String author;
    private int currentPage;

    public String getTitle() {
        return this.title;
    }

    public String getAuthor() {
        return this.author;
    }

    public void turnPage() {
        this.currentPage += 1;
    }

    public String printCurrentPage() {
        return "currentPage:" + this.currentPage + "content";
    }
}