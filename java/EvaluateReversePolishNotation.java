public class EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens) {
        if (tokens == null) {
            return 0;
        }
    
        String operations = "+-*/";
        Stack<Integer> stack = new Stack<Integer>();
        for (String token : tokens) {
            if (operations.contains(token)) {
                int a = stack.pop();
                int b = stack.pop();
                int index = operations.indexOf(token);
                switch (index) {
                    case 0:
                        stack.push(b + a);
                        break;
                    case 1:
                        stack.push(b - a);
                        break;
                    case 2:
                        stack.push(b * a);
                        break;
                    case 3:
                        stack.push(b / a);
                        break;
                }
            } else {
                stack.push(Integer.valueOf(token));
            }
        }
        
        return stack.pop();
    }
}
