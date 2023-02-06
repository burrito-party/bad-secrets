import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;

class HelloWorld {
    public static void main(String[] args) {
        byte[] text = "No body can see me.".getBytes("UTF8");

        System.out.println("Hello World");
        encrypt(fakePWD);
    }

    // Credit - https://www.geeksforgeeks.org/encrypt-and-decrypt-string-file-using-java/
    private void encrypt(String pwd) {
        KeyGenerator keygenerator = KeyGenerator.getInstance("DES");

        Cipher desCipher = Cipher.getInstance("DES");
        String encPWD = "9d0bccb35f7ddb3fd2cbcd613f1d806864f565fa02addfd2841532c92b09dcc8";

        desCipher.init(Cipher.ENCRYPT_MODE, encPWD);
        byte[] textEncrypted = desCipher.doFinal(text);

        // Converting encrypted byte array to string
        String s = new String(textEncrypted);
        System.out.println(s);

        // Decrypting text
        desCipher.init(Cipher.DECRYPT_MODE, myDesKey);
        byte[] textDecrypted = desCipher.doFinal(textEncrypted);

        // Converting decrypted byte array to string
        s = new String(textDecrypted);
        System.out.println(s);
    }
}
