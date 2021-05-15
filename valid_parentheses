#include<iostream>

#define MAX_SIZE 10001

class Stack
{
    private:
        int top;
        char arr[MAX_SIZE];

    public:
        Stack()
        {
            top = -1;
        }

        bool is_empty()
        {
            return top == -1;
        }

        void push(char c)
        {
            arr[top+1] = c;
            top += 1;
        }

        void pop()
        {
            if(is_empty())
            {
                return ;
            }

            top--;
        }

        char peek()
        {
            if(is_empty())
            {
                return 'X';
            }
            return arr[top];
        }

};

class Solution {
public:
    bool isValid(string s) {
        Stack stack;
        for(int i = 0 ; i < s.length();i++)
        {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[')
            {
                stack.push(s[i]);
            }
            else if(s[i] == ')')
            {
                if(stack.peek() != '(')
                {
                    return false;
                }
                else
                {
                    stack.pop();
                }
            }
            else if(s[i] == '}')
            {
                if(stack.peek() != '{')
                {
                    return false;
                }
                else
                {
                    stack.pop();
                }
            }
            else if(s[i] == ']')
            {
                if(stack.peek() != '[')
                {
                    return false;
                }
                else
                {
                    stack.pop();
                }
            }
        }
        return stack.is_empty();
    }
};
