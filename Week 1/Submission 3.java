import java.util.Scanner;
public class Main
{
    public static void main(String[] args) {
    int ans;
    Scanner sc= new Scanner(System.in);
    System.out.println("Please enter 5 digits for input");
    System.out.println("The largest product which can be formed from any three of them shall be output");
    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();
    int d = sc.nextInt();
    int e = sc.nextInt();
    ans = Math.max(a*b*c, Math.max(a*b*d, Math.max(a*b*e, Math.max(a*c*d, Math.max(a*c*e, Math.max(a*d*e, Math.max(b*c*d, Math.max(b*c*e, Math.max(b*d*e, c*d*e)))))))));
 
    System.out.println("The largest possible product of provided digits is "+ ans);
    }
}
