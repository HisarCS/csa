public class ConversionChart {
    public static void main(String[] args) throws Exception {


    System.out.println("HHH");
    System.out.println(binaryToHex("011110101010"));
    System.out.println(asciiToBinary("PLANT"));
    System.out.println(decimalToBinary(64));
    System.out.println(octalToHex("5123"));


}
   

    public static String decimalToBinary(int d) {	 
        String b = Integer.toBinaryString(d);
        while(b.length()<8) {
            b = "0" + b;
        }
        return b;	
   }


   public static String asciiToBinary(String ascii) 
			{
				String asc = "";
				for(int i = 0; i<=ascii.length()-1;i++) {
					 char a = ascii.charAt(i);
					  asc += decimalToBinary(a) + " ";
				}
				
				return asc;
				
            }
    

    public static String binaryToHex(String binary) { 
        while((binary.length() % 4) != 0) {
            binary = "0" + binary;
        }
        int decimal = Integer.parseInt(binary,2);
        String hex = Integer.toString(decimal,16);
        
        return hex;
    }

    public static String octalToHex(String octal) {
        int decimal = octalToDecimal(octal);
        String hex = Integer.toHexString(decimal);
        return hex;
    }

    public static int octalToDecimal(String octal) {
        int decimal = Integer.parseInt(octal,8);
        return decimal;
    }
    

}
