package Security.coPhuongWriteUp;

import java.util.Scanner;

public class CapSoThanThiet {
    
    static Scanner scanner = new Scanner(System.in);

    public static long sumOfDivisior(long n) {
        long sum = 1;
        for (long i = 2; i*i < n; i++) {
            if (n % i == 0) {
                if (n / i == i) {
                    sum += 1;
                }else{
                    sum += (i + (n / i));
                }
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        long n;
        n = scanner.nextLong();
        for (long i = 1; i <= n; i++) {
            long a = sumOfDivisior(i);
            if (i == sumOfDivisior(a) && a != i && a < n && i < a) {
                System.out.println(i + " " + a);
            }
        }
    }
}
