using System;
using System.Collections.Generic;
using System.Linq;

namespace Program_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] ListOfNumbers = { 1831, 1675, 1978, 1923, 1648, 1972, 2008, 1967, 2006, 1980, 1896, 1911, 2004, 1857, 1882, 1609, 1764, 1774, 1970, 1949, 1983, 1889, 1835, 1852, 2002, 829, 1916, 1884, 1808, 1996, 1956, 1633, 1855, 167, 1903, 1873, 1783, 1945, 1725, 143, 1906, 1701, 1974, 1924, 1890, 1584, 1999, 1871, 2007, 1643, 1729, 1874, 1920, 1791, 1904, 1832, 1958, 1862, 1910, 1919, 1940, 1897, 1891, 1918, 1936, 1992, 1950, 1807, 1737, 1968, 1925, 1869, 1784, 1973, 603, 1881, 1909, 1638, 1786, 1953, 1887, 1969, 1957, 1984, 1962, 1955, 1850, 1875, 1948, 1191, 1902, 1954, 1663, 1915, 1995, 2005, 1943, 1892, 1993, 1616, 1883, 1986, 1960, 1894, 1952, 1927, 1964, 1997, 1899, 697, 1694, 1685, 1921, 1905, 1963, 1965, 1859, 1753, 1876, 1900, 1990, 830, 1712, 2009, 1810, 1929, 1914, 418, 1994, 1998, 1987, 1961, 1933, 1872, 657, 1979, 76, 1982, 1931, 1926, 1938, 1930, 1932, 1985, 1870, 1988, 1939, 1951, 1833, 2001, 1975, 1898, 1893, 1907, 1977, 1935, 1941, 1901, 1776, 1981, 1912, 2000, 1971, 1885, 1718, 1976, 1803, 1913, 1922, 1611, 1687, 1942, 1908, 1880, 1828, 1182, 1959, 1966, 1707, 1604, 1917, 1991, 1947, 1781, 1937, 1934, 1856, 945, 2003, 1614, 1946, 431, 1989, 2010, 367, 1878, 1658, 1660, 1732, 1895 };
            int year = 2020;
           






            for (int i = 0; i < 200; i++)
            {
                for (int x = 0; x < 200; x++)
                {
                    for (int z = 0; z < 200; z++)
                    {
                        if (ListOfNumbers[i] + ListOfNumbers[x] + ListOfNumbers[z] == 2020)
                        {
                            Console.WriteLine(ListOfNumbers[i]);
                            Console.WriteLine(ListOfNumbers[x]);
                            Console.WriteLine(ListOfNumbers[z]);
                        }
                    }
                    
                }

            }

            
           


            Console.ReadKey();
        }

    }
}