package srpexam.srp;

public class HtmlPrinter implements Printer{

    private Book book;

    public HtmlPrinter(Book book) {
        this.book = book;
    }

    @Override
    public String printPage(Book book) {
        return "curPage is :" + book.getCurrentPage() + "HtmlPrinter content";
    }
}
