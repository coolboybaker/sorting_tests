using System;

public class Program
{
    public static void Main(string[] args)
    {
        int a = 5;
        int b = 8;
        a = a + b;
        b = a - b;
        a = a - b;
        Console.WriteLine (a + " " + b);
    }
}
