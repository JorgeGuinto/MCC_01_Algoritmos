import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Elemento e1 = new Elemento(79, 85);
        Elemento e2 = new Elemento(32, 26);
        Elemento e3 = new Elemento(47, 48);
        Elemento e4 = new Elemento(18, 21);
        Elemento e5 = new Elemento(26, 22);
        Elemento e6 = new Elemento(85, 95);
        Elemento e7 = new Elemento(33, 43);
        Elemento e8 = new Elemento(40, 45);
        Elemento e9 = new Elemento(45, 55);
        Elemento e10 = new Elemento(59, 52);

        ArrayList <Elemento> elementos = new ArrayList<>();
        elementos.add(e1);
        elementos.add(e2);
        elementos.add(e3);
        elementos.add(e4);
        elementos.add(e5);
        elementos.add(e6);
        elementos.add(e7);
        elementos.add(e8);
        elementos.add(e9);
        elementos.add(e10);

        Mochila mochila = new Mochila(140);
        Mochila mochilaOptima = new Mochila(140);

        llenarMochila(mochila, mochilaOptima, elementos, false);
        System.out.println(mochilaOptima.toString());
    }

    public static void llenarMochila(Mochila prueba, Mochila optima, ArrayList<Elemento> elementos, boolean llena) {
        if (llena) {
            if (prueba.getValorTotal() > optima.getValorTotal()) {
                ArrayList<Elemento> elementosOpt = prueba.getElementos();
                optima.vaciarMochila();
                for (Elemento e: elementosOpt) {
                    optima.agregarElemento(e);
                }
            }
        } else {
            for (int i = 0; i < elementos.size(); i++) {
                if (!prueba.checkElemento(elementos.get(i))) {
                    //No está en la mochila
                    if(prueba.getPesoMaximo() >= prueba.getPesoTotal() + elementos.get(i).getPeso()){
                        //Sí cabe, lo podemos agregar
                        prueba.agregarElemento(elementos.get(i));
                        llenarMochila(prueba, optima, elementos, false);
                        prueba.eliminarElemento(elementos.get(i));
                    } else {
                        llenarMochila(prueba, optima, elementos, true);
                    }
                }
            }
        }
    }
}