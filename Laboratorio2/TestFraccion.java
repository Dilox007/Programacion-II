public class TestFraccion {

    public static void main(String[] args) {

        // Crear algunas fracciones
        Fraccion f1 = new Fraccion(1, 4);
        Fraccion f2 = new Fraccion(4, 3);

        System.out.println("Fraccion 1: " + f1);
        System.out.println("Fraccion 2: " + f2);

        // operaciones básicas
        Fraccion s = f1.suma(f2);
        System.out.println("Suma: " + s);

        Fraccion r = f1.resta(f2);
        System.out.println("Resta: " + r);

        // multiplicacion
        Fraccion m = f1.multiplica(f2);
        System.out.println("Multiplicacion: " + m);

        // division
        Fraccion d = f1.divide(f2);
        System.out.println("Division: " + d);

        // convertir a decimal
        double dec = f1.convertirADecimal();
        System.out.println("Decimal de f1: " + dec);

        // probar inverso
        boolean inv = f1.esInverso(f2);
        System.out.println("Son inversos?: " + inv);

        // probar parse
        Fraccion f3 = Fraccion.parseFraccion("-2/3");
        System.out.println("parseFraccion: " + f3);

        // probar simplificacion
        Fraccion f4 = new Fraccion(2, 8);
        System.out.println("Fraccion antes de simplificar: " + f4);

        Fraccion simplificada = f4.simplifica();
        System.out.println("Fraccion simplificada: " + simplificada);

    }
}