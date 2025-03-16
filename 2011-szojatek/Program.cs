using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace szavak

{
	class Program
	{
		static void Main(string[] args)
		{
			string szo;
			Console.WriteLine("1. feladat");
			Console.Write("Kerek egy szot: ");
			szo = Console.ReadLine();
			int i = 0;
			int h = szo.Length;
			while (i <= h - 1 && !(szo[i] == 'a' || szo[i] == 'e' || szo[i] == 'i' || szo[i] == 'o' || szo[i] == 'u'))
				i++;
			if (i > h - 1) Console.WriteLine("Nem tartalmaz maganhangzot");
			else Console.WriteLine("Tartalmaz maganhangzot");
			int maxertek = 0;
			string leghosszabbszo = "";
			h = 0;
			int dbszo = 0;
			int dbtobbmaganh = 0;
			string[] otkarakteres = new String[1000];
			int otkarelemszam = -1;	
			Console.WriteLine();
			Console.WriteLine("3. feladat");
			StreamReader be = new StreamReader("szoveg.txt");
			szo = be.ReadLine();
			while (szo != null)
			{
				h = szo.Length;
				dbszo++;
				if (maxertek < h)
				{
					maxertek = h;
					leghosszabbszo = szo;
				}
				int db =0;
				for (i = 0; i <= h - 1; i++)
					if (szo[i] == 'a' || szo[i] == 'e' || szo[i] == 'i' || szo[i] == 'o' || szo[i] == 'u')
					db++;
				if (db > h - db)
				{
					dbtobbmaganh++;
					Console.Write("{0} ", szo);
				}
				if (h == 5)
				{
					otkarelemszam++;
					otkarakteres[otkarelemszam] = szo;
					
				}
				szo = be.ReadLine();
				

			}	
			be.Close();
			float szazalek = 100 * (float)dbtobbmaganh / (float)dbszo;
			Console.WriteLine();
			Console.WriteLine("{0}/{1} : {2:N2}", dbtobbmaganh, dbszo, szazalek);
			Console.WriteLine("2. feladat");
            Console.WriteLine("A leghosszabb szo: {0}", leghosszabbszo);
			Console.WriteLine();
			Console.WriteLine("4. feladat");
            string harombetus;
			Console.WriteLine("Kerek egy harombetus szoreszletet: ");
			harombetus = Console.ReadLine();
			Console.WriteLine("Hozza tartozo otkarakteres szavak: ");
			for (i = 0; i <= otkarelemszam; i++)
                if (otkarakteres[i].Substring(1, 3) == harombetus)
                    Console.Write("{0} ", otkarakteres[i]);
            Console.WriteLine();
			Console.WriteLine("5. feladat");
            int j;
            string csere;
			StreamWriter ki = new StreamWriter("letra.txt");
			for (i = 0; i <= otkarelemszam - 1; i++)
                for (j = otkarelemszam; j > i; j--)
                    if (String.Compare(otkarakteres[j - 1].Substring(1, 3), otkarakteres[j].Substring(1, 3)) == 1)
                    {
                        csere = otkarakteres[j];
                        otkarakteres[j] = otkarakteres[j - 1];
                        otkarakteres[j - 1] = csere;
                    }
			if (otkarakteres[0].Substring(1, 3) == otkarakteres[1].Substring(1, 3))
                ki.WriteLine(otkarakteres[0]);
			for (i = 1; i <= otkarelemszam - 2; i++)
            {
                if (otkarakteres[i].Substring(1, 3) == otkarakteres[i - 1].Substring(1, 3)
                || otkarakteres[i].Substring(1, 3) == otkarakteres[i + 1].Substring(1, 3))
                    ki.WriteLine(otkarakteres[i]);
                if (otkarakteres[i].Substring(1, 3) != otkarakteres[i + 1].Substring(1, 3)
                && otkarakteres[i].Substring(1, 3) == otkarakteres[i - 1].Substring(1, 3))
                    ki.WriteLine();
            }
			if (otkarakteres[i].Substring(1, 3) == otkarakteres[i + 1].Substring(1, 3))
                ki.WriteLine(otkarakteres[i + 1]);
            ki.Flush();
            ki.Close();
            Console.WriteLine("Elkeszult a letra.txt fajl.");
            Console.ReadLine();
		}
	}
}
		

