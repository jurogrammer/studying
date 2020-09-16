package composite.goods;

public class MakeComposite {

    public static Goods getComposite() {
        //Box의 method를 사용하기 위해 변수를 Box타입으로 선언
        Box box1 = new Box("box1");
        Box box2 = new Box("box2");
        Box box3 = new Box("box3");
        Box box4 = new Box("box4");
        Goods headSet1 = new HeadSet("headSet1");
        Goods noteBook1 = new NoteBook("noteBook1");
        Goods pencil1 = new Pencil("pencil1");
        Goods water1 = new Water("water1");

        box4.addItems(headSet1);

        box3.addItems(box4);
        box3.addItems(water1);

        box2.addItems(pencil1);

        box1.addItems(box3);
        box1.addItems(box2);
        box1.addItems(noteBook1);

        return box1;
    }
}
