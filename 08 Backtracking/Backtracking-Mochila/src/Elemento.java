public class Elemento {
    private int peso;
    private int valor;

    public Elemento(int valor, int peso) {
        this.peso = peso;
        this.valor = valor;
    }

    public int getPeso() {
        return peso;
    }

    public int getValor() {
        return valor;
    }

    public boolean equals(Elemento elemento) {
        if (this.peso == elemento.getPeso() && this.valor == elemento.getValor()){
            return true;
        } else {
            return false;
        }
    }

    @Override
    public String toString() {
        return "Peso: " + peso +
                ", valor: " + valor;
    }
}