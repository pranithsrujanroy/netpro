/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package serialization;
import java.io.*;
/**
 *
 * @author Student
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
    public static void main(String[] args) {
        // TODO code application logic here
        Student stu1 = new Student("Sita", 23);
        Student stu2 = new Student("Gita", 24);
        String stud1 = "stu1.txt", stud2 = "stu2.txt";
        //Serializing stu1
        try{
            FileOutputStream file = new FileOutputStream(stud1); 
            ObjectOutputStream out = new ObjectOutputStream(file); 
              
            // Method for serialization of object 
            out.writeObject(stu1); 
              
            out.close(); 
            file.close(); 
              
            System.out.println("Student1 has been serialized"); 
        }
        catch(IOException ex){
            System.out.println("IOException is caught");
        }
        //Serializing stu2
        try{
            FileOutputStream file2 = new FileOutputStream(stud2);
            ObjectOutputStream out2 = new ObjectOutputStream(file2);
            //Serializing stu2 object
            out2.writeObject(stu2);
            out2.close();
            file2.close();
            
            System.out.println("Student2 has been serialized");
        }
        catch(IOException ex){
            System.out.println("IOException is caught");
        }
        
        //Deserializing
        Student st1 = null;
        Student st2 = null;
        try{
            FileInputStream f1 = new FileInputStream(stud1);
            ObjectInputStream i1 = new ObjectInputStream(f1);
            
            st1 = (Student)i1.readObject();
            
            i1.close();
            f1.close();
            
            System.out.println("Student1 has been deserialized");
            System.out.println("Name: "+st1.name);
            System.out.println("age: "+st1.age);
        }
        catch(Exception ex){
            System.out.println("Exception caught while deserializing student1 object");
        }
        
        try{
            FileInputStream f2 = new FileInputStream(stud2);
            ObjectInputStream i2 = new ObjectInputStream(f2);
            
            st2 = (Student)i2.readObject();
            
            i2.close();
            f2.close();
            
            System.out.println("Student2 has been deserialized");
            System.out.println("Name: "+st2.name);
            System.out.println("age: "+st2.age);
        }
        catch(Exception e){
            System.out.println("Exception caught while deserializing student2");
        }
    }
    
}
