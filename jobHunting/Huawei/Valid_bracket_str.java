import java.util.Scanner;
import java.util.Stack;

public class Valid_bracket_str {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        // String str = "((()())()()(";
        System.out.print(longlengthstr(str));
    }
    
    public static int longlengthstr(String str){
        if(str == null||str.length() == 0)
            return 0;
        Stack<Integer> stack = new Stack<Integer>();
        int begin     = 0;
        int maxLength = 0;

        for(int i = 0; i < str.length(); i++)
        {
            if(str.charAt(i) == '('){
                stack.push(i);
            }
            // currrent char is not '(' and the stack is empty,
            // ignore the current char and move the begin index to the next position.
            else if(stack.isEmpty()){
                begin = i + 1;
            }
            else if(str.charAt(i) == ')')  // with some '('s in the stack.
            {
                stack.pop(); // pop a matching '('
                if(stack.isEmpty())
                    maxLength = Math.max(maxLength, i-begin+1);
                else
                    maxLength = Math.max(maxLength, i-stack.peek());
            }
            else // got other char, rather than '(' or ')',
            {    // then all the previous chars cannot be connected
                 // with the rest ones, thus the stack should be emptied.
                while(!stack.isEmpty())
                {
                    stack.pop();
                }
                begin = i+1;
            }
        }
        return maxLength; 
    }

}