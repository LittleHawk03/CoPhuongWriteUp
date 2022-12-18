package Security.coPhuongWriteUp;

import java.util.Scanner;

public class LuyThuaBacB {

    static Scanner scanner = new Scanner(System.in);
    static long p = 1000000007;

    public static long squater_loop2(long a, long k) {
        long b = 1;
        a = a % p;
        while (k > 0) {
            if (k % 2 == 1) {
                b = (b * a) % p;
            }    
            k = k / 2;
            a = (a * a) % p;
        }
        return b;
    }

    public static void main(String[] args) {
        long a = scanner.nextLong();
        long b = scanner.nextLong();
        System.out.println(squater_loop2(a, b));
    }
}
