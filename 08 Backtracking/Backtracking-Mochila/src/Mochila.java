import java.util.ArrayList;

public class Mochila {
    private int pesoMaximo;
    private ArrayList<Elemento> elementos;
    private int valorTotal;
    private int pesoTotal;

    public Mochila(int pesoMaximo) {
        this.pesoMaximo = pesoMaximo;
        this.elementos = new ArrayList<>();
        this.valorTotal = 0;
        this.pesoTotal = 0;
    }

    public int getPesoMaximo() {
        return pesoMaximo;
    }
    public ArrayList<Elemento> getElementos() {
        return elementos;
    }
    public int getValorTotal() {
        return valorTotal;
    }
    public int getPesoTotal() {
        return pesoTotal;
    }

    public void agregarElemento (Elemento nuevoElemento) {
        this.elementos.add(nuevoElemento);
        this.pesoTotal += nuevoElemento.getPeso();
        this.valorTotal += nuevoElemento.getValor();
    }

    public boolean checkElemento (Elemento elemento) {
        for (int i = 0; i < this.elementos.size(); i++) {
            if (elementos.get(i).equals(elemento)){
                return true;
            }
        }
        return false;
    }

    public void vaciarMochila(){
        while (this.elementos.size()>0){
            this.elementos.remove(0);
        }
        this.valorTotal = 0;
        this.pesoTotal = 0;
    }

    public void eliminarElemento(Elemento elemento) {
        for (int i = 0; i < this.elementos.size(); i++) {
            if (this.elementos.get(i) == elemento) {
                this.elementos.remove(i);
                this.pesoTotal = this.pesoTotal - elemento.getPeso();
                this.valorTotal = this.valorTotal - elemento.getValor();
            }
        }
    }

    @Override
    public String toString() {
        String lista = "Mochila: \n";
        for (Elemento e: this.elementos) {
            lista = lista + "Valor: " + e.getValor() + " Peso: " + e.getPeso() + "\n";
        }
        lista = lista + "valorTotal=" + valorTotal +
                ", pesoTotal=" + pesoTotal +
                '}';
        return lista;
    }
}