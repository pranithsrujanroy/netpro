/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package serialization;
import java.io.*;
/**
 *
 * @author Pranith Srujan Roy
 */
public class Student implements java.io.Serializable{
    /**
     * @param args the command line arguments
     */
    String name;
    int age;
    Student(String name, int age){
        this.name = name;
        this.age = age;
    }
    void serializeStudent(Student stu, String file){
        try{
            FileOutputStream f = new FileOutputStream(file);
            ObjectOutputStream o = new ObjectOutputStream(f);
            
            o.writeObject(stu);
            
            o.close();
            f.close();
            System.out.println(stu.name + " object serialized");
        }
        catch(IOException e){
            System.out.println("IOException caught");
        }
    }
    
    Student deSerializeStudent(String file){
        Student stu = null;
        try{
            FileInputStream f = new FileInputStream(file);
            ObjectInputStream i = new ObjectInputStream(f);
            
            stu = (Student)i.readObject();
            
            i.close();
            f.close();
            
            System.out.println(stu.name + " object deserialized");
        }
        catch(Exception e){
            System.out.println("Exception caught");
        }
        return stu;
    }
    
    void printObject(Student stu){
        System.out.println("Name: "+stu.name);
        System.out.println("Age: "+stu.age);
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        Student stu1 = new Student("Sita", 23);
        Student stu2 = new Student("Gita", 24);
        String stud1 = "stu1.txt", stud2 = "stu2.txt";
        //Serializing Student objects
        stu1.serializeStudent(stu1, stud1);
        stu2.serializeStudent(stu2, stud2);
        //Deserializing
        Student st1 = null;
        Student st2 = null;
        stu1 = stu1.deSerializeStudent(stud1);
        stu1.printObject(stu1);
        
        stu2 = stu2.deSerializeStudent(stud2);
        stu2.printObject(stu2);
    }
}
