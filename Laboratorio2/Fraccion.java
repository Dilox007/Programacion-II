/**
 * La Clase Fraccion.
 *
 * @author Dilan Thomas Chura Cala
 */
public class Fraccion {

    // Atributos
    private int numerador;
    private int denominador;

    // Métodos

    /**
     * Construye una nueva fracción.
     */
    public Fraccion() {
        this.numerador = 0;
        this.denominador = 1;
    }

    /**
     * Construye una nueva fracción.
     */
    public Fraccion(int n, int d) {
        this.numerador = n;
        this.denominador = d;
    }

    /**
     * Comprueba si dos fracciones son iguales.
     *
     * @param o Object, otro objeto.
     * @return true si las fracciones son iguales.
     */
    @Override
    public boolean equals(Object o) {
        if (o instanceof Fraccion) {
            Fraccion f = (Fraccion) o;
            return f.numerador == this.numerador &&
                   f.denominador == this.denominador;
        } else {
            return false;
        }
    }

    /**
     * Retorna la representación de cadena del objeto Fraccion.
     *
     * @return String, la fracción en formato de cadena.
     */
    @Override
    public String toString() {
        return String.format("%d/%d", this.numerador, this.denominador);
    }

    /**
     * Suma dos fracciones.
     *
     * @param o Fraccion, contiene la otra fracción.
     * @return Fraccion resultante.
     */
    public Fraccion suma(Fraccion o) {
        int n = (this.numerador * o.denominador) +
                (this.denominador * o.numerador);

        int d = this.denominador * o.denominador;

        return new Fraccion(n, d);
    }

    /**
     * Resta dos fracciones.
     *
     * @param o Fraccion, contiene la otra fracción.
     * @return c Fraccion resultante.
     */
    public Fraccion resta(Fraccion o) {
        Fraccion c = new Fraccion();

        c.numerador = (this.numerador * o.denominador) -
                      (this.denominador * o.numerador);

        c.denominador = this.denominador * o.denominador;

        return c;
    }

    /*
     a) Multiplica dos fracciones.
     */
    public Fraccion multiplica(Fraccion o) {
        int n = this.numerador * o.numerador;
        int d = this.denominador * o.denominador;

        return new Fraccion(n, d);
    }

    /*
     b) Divide dos fracciones.
     */
    public Fraccion divide(Fraccion o) {
        int n = this.numerador * o.denominador;
        int d = this.denominador * o.numerador;

        return new Fraccion(n, d);
    }

    /*
     c) Convierte la fracción a decimal.
     */
    public double convertirADecimal() {
        if (this.denominador == 0) {
            throw new ArithmeticException("No se puede dividir entre 0");
        }

        return (double) this.numerador / this.denominador;
    }

    /*
     d) Verifica si dos fracciones son inversas.
     */
    public boolean esInverso(Fraccion o) {
        Fraccion r = this.multiplica(o);
        return r.numerador == r.denominador;
    }

    /*
     e) Convierte una cadena a objeto Fraccion.
     */
    public static Fraccion parseFraccion(String str) {
        String[] partes = str.split("/");

        int n = Integer.parseInt(partes[0]);
        int d = Integer.parseInt(partes[1]);

        return new Fraccion(n, d);
    }

    /*
     f) Simplifica una fracción.
     */
    public Fraccion simplifica() {
        int mcd = mcd(this.numerador, this.denominador);

        int n = this.numerador / mcd;
        int d = this.denominador / mcd;

        return new Fraccion(n, d);
    }

    /*
     Método auxiliar para calcular el MCD.
     */
    private int mcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }
}