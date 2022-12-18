package Security.coPhuongWriteUp;

import java.util.Scanner;

public class SieuSoNguyenTo {

    static Scanner scanner = new Scanner(System.in);

    public static boolean solution(int n) {
        Boolean[] isPrime = new Boolean[n + 1];
        if (n < 0) {
            return false;
        }
        isPrime[0] = false;
        if (n + 1 > 1) {
            isPrime[1] = false;
        }
        for (int i = 2; i < isPrime.length; i++) {
            isPrime[i] = true;
        }

        for (int i = 2; i*i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i*i; j <= n; j+= i) {
                    isPrime[j] = false;
                }
            }
        }

        int count = 0;

        for (int i = 2; i < n; i++) {
            if (isPrime[i]) {
                count++;
            }
        }

        return isPrime[count];
    }


    public static void main(String[] args) {
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        int count = 0;
        for (int i = a; i <= b; i++) {
            if (solution(i)) {
                count++;
            }
        }

        System.out.println(count);
    }
    
}
