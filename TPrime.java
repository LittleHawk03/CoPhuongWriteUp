package Security.coPhuongWriteUp;

import java.util.Scanner;

public class TPrime {
    
    static Scanner scanner = new Scanner(System.in);

    public static Boolean checkChinhPhuong(int n) {
        int i = (int) Math.sqrt(n);
        return i*i == n;
    }

    public static void main(String[] args) {
        int n;
        n = scanner.nextInt();
        for (int i = 2; i < n; i++) {
            if (checkChinhPhuong(i)) {
                System.out.println(i);
            }
        }
        
    }
}
