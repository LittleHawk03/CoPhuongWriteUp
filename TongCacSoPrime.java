package Security.coPhuongWriteUp;
import java.util.Scanner;

public class TongCacSoPrime {
    static Scanner scanner = new Scanner(System.in);

    public static void solution(int a,int b) {
        boolean[] isPrime = new boolean[b - a + 1];

        long sum = 0;
        for (int i = 0; i < b - a + 1; i++) {
            isPrime[i] = true;
        }

        for (int i = 2; i*i <= b; i++) {
            for (int j = Math.max(i*i,(a + i - 1)/i * i); j <= b; j+=i) {
                isPrime[j - a] = false;
            }
        }

        if (a <= 1) {
            isPrime[1 - a] = false;
        }

        for (int i = a; i <= b; i++) {
            if (isPrime[i - a]) {
                sum += i;
            }
        }
        System.out.println(sum);
    }

    public static void main(String[] args) {
        int a,b;
        a = scanner.nextInt();
        b = scanner.nextInt();
        solution(a, b);
    }
}
