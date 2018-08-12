/*
Given a sequence of integer, figure out how many time
it will take to fetch all of them. Each time all the
integers to take out must be in ascending order in the
current sequence.
*/



import java.util.ArrayList;
import java.util.Scanner;

public class MinNumSequence {

    private static int min = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n        = scan.nextInt();
        min          = n;
        int[] list   = new int[n];
        for(int i = 0; i < n; i++) {
            list[i] = scan.nextInt();
        }
        search(list, 0);
        System.out.println(min);
    }


    private static void search(int[] integers, int count) {
        count ++;
        if(count > min)
            return;

        ArrayList<Integer> copy = new ArrayList<Integer>();
        for(Integer i :integers) {
            copy.add(i);
        }

        //升序规则 
        for(int i = integers.length - 1; i >= 0; i--) {
            if(i == 0) {
                if(integers[i] > Integer.MIN_VALUE) {
                    copy.remove(i);
                }
            }
            else if(integers[i] > integers[i-1]) {
                copy.remove(i);
            }
        }
        if(copy.size() == 0) {
            if(count < min) {
                min = count;
            }
            return;
        }
        int[] copyArray = new int[copy.size()];
        for(int i = 0; i < copy.size(); i++) {
            copyArray[i] = copy.get(i);
        }
        search(copyArray, count);
        copy.clear();
        for(Integer i : integers) {
            copy.add(i);
        }

        //降序规则
        //升序规则 
        for(int i=integers.length-1;i>=0;i--) {
            if(i==0) {
                if(integers[i]<Integer.MAX_VALUE) {
                    copy.remove(i);
                }
            }
            else if(integers[i]<integers[i-1]) {
                copy.remove(i);
            }
        }
        if(copy.size()==0) {
            if(count<min) {
                min=count;
            }
            return;
        }

        copyArray = new int[copy.size()];
        for(int i =0;i<copy.size();i++) {
            copyArray[i]=copy.get(i);
        }
        search(copyArray,count);    
    }
}
