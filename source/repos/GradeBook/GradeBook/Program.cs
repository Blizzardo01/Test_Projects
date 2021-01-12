using System;
using System.Collections.Generic;

namespace GradeBook
{
    class Program
    {
        static void Main(string[] args)
        {
            var book = new Book();
            book.AddGrade(90.1);

            var grades = new List<double>() { 12, 10, 5, 8 };
            grades.Add(56.0);
            
            double result = 0.0;
            foreach (var number in grades)
            {
                result += number;
            }
            result = result /= grades.Count;
            Console.WriteLine($"The average grade is {result:N1}");
         
        }
    }
}