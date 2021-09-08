using System;

namespace Program_2
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] allData = System.IO.File.ReadAllLines("C:/Users/Jan Graffe/Desktop/Advent of programming/Program 2/Program 2/allData.txt");
            string[] minNumbers = { "0" };
            for (int i = 0; i < 200; i++)
            {
                minNumbers = allData[i].Split('2');
                
            }
            for (int x = 0; x < minNumbers.Length; x++) 
            {
                 allData[x] = minNumbers[x];
            }
            /*for (int z = 0; z < minNumbers.Length; z++)
            {
                Console.WriteLine(minNumbers[z]);
            }*/
            for (int y = 0; y < allData.Length; y++)
            {
                Console.WriteLine(allData[y]);
            }



            Console.ReadKey();
        }
    }
}
