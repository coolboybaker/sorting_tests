// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        string input = Console.ReadLine();
        bool isSuccess = true;
        for (int i = 0; i < input.Length; i++)
        {
            if (IsAllowed(input[i]) == false)
            {
                throw new Exception("Поле содержит недопустимый символ!");
            }
        }
    }
    public static bool IsAllowed(char L)
    {
        string allowedNumbers = "0123456789";
        for (int i = 0; i < 10; i++)
        {
            if (L == allowedNumbers[i])
            return true;
        }
        return false;
    }
}
