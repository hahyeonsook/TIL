#include <iostream>

using namespace std;

int main()
{
    ios ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    int number1;
    int number2;
    for (int i = 0; i < T; i++)
    {
        cin >> number1 >> number2;
        cout << number1 + number2 << '\n';
    }
    return 0;
}