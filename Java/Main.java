import java.util.function.BiFunction;

public class Main {
    public static void main(String[] args) {
        timing(1000000);
    }

    public static double[] eulerMethod(BiFunction<Double, Double, Double> func, int iterations, double step) {
        double x=0;
        for (int i = 0; i < 200; i++) {
            x = 1 + 1;
        }
        return new double[]{x};
    }

    public static double[] eulerImprovedMethod(BiFunction<Double, Double, Double> func, int iterations, double step) {
        double x=0;
        for (int i = 0; i < 200; i++) {
            x = 1 + 1;
        }
        return new double[]{x};
    }

    public static double[] RK4(BiFunction<Double, Double, Double> func, int iterations, double step) {
        double x=0;
        for (int i = 0; i < 200; i++) {
            x = 1 + 1;
        }
        return new double[]{x};
    }

    public static void timing(int iterations) {
        double RK4TimeTotalDummy = 0;
        for (int i = 0; i < 100000; i++) {
            long startRK4 = System.nanoTime();
            RK4((x, y) -> x + y, 1, 1);
            long endRK4 = System.nanoTime();
            double RK4Time = (endRK4 - startRK4) / 1e6;
            RK4TimeTotalDummy += RK4Time;
        }

        double RK4TimeTotal = 0;
        // Timing RK4
        for(int i = 0; i<iterations; i++){
            long startRK4 = System.nanoTime();
            RK4((x, y) -> x + y, 1, 1);
            long endRK4 = System.nanoTime();
            double RK4Time = (endRK4 - startRK4) / 1e6;
            RK4TimeTotal += RK4Time;
        }

        double EulerTimeTotalDummy = 0;
        for(int i = 0; i<iterations; i++){
            // Timing eulerMethod
            long startEuler = System.nanoTime();
            eulerMethod((x, y) -> x + y, 1, 1);
            long endEuler = System.nanoTime();
            double eulerTime = (endEuler - startEuler) / 1e6;
            EulerTimeTotalDummy += eulerTime;
        }

        double EulerTimeTotal = 0;
        for(int i = 0; i<iterations; i++){
            // Timing eulerMethod
            long startEuler = System.nanoTime();
            eulerMethod((x, y) -> x + y, 1, 1);
            long endEuler = System.nanoTime();
            double eulerTime = (endEuler - startEuler) / 1e6;
            EulerTimeTotal += eulerTime;
        }


        double eulerImprovedTimeTotalDummy = 0;
        for(int i = 0; i < iterations; i++){
            // Timing eulerImprovedMethod
            long startEulerImproved = System.nanoTime();
            eulerImprovedMethod((x, y) -> x + y, 1, 1);
            long endEulerImproved = System.nanoTime();
            double eulerImprovedTime = (endEulerImproved - startEulerImproved) / 1e6;
            eulerImprovedTimeTotalDummy+=eulerImprovedTime;
        }

        double eulerImprovedTimeTotal = 0;
        for(int i = 0; i < iterations; i++){
            // Timing eulerImprovedMethod
            long startEulerImproved = System.nanoTime();
            eulerImprovedMethod((x, y) -> x + y, 1, 1);
            long endEulerImproved = System.nanoTime();
            double eulerImprovedTime = (endEulerImproved - startEulerImproved) / 1e6;
            eulerImprovedTimeTotal+=eulerImprovedTime;
        }

        

        // Printing results
        System.out.printf("Euler metode tid gns: %.5f ms%n", EulerTimeTotal/iterations);
        System.out.printf("Euler forbedret metode tid gns: %.5f ms%n", eulerImprovedTimeTotal/iterations);
        System.out.printf("RK4 tid gns: %.5f ms%n", RK4TimeTotal/iterations);
        System.out.printf("%.5f ms%n",RK4TimeTotalDummy, EulerTimeTotalDummy, eulerImprovedTimeTotalDummy);
    }
}
