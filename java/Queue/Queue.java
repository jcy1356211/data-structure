public interface Queue<E> {

    void enqueue(E e);
    int getSize();
    E dequeue();
    E getFront();
    boolean isEmpty();
}
