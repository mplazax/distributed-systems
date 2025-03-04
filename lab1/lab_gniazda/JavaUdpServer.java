import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Arrays;

public class JavaUdpServer {

    public static void main(String args[])
    {
        System.out.println("JAVA UDP SERVER");
        DatagramSocket socket = null;
        int portNumber = 9008;

        try{
            socket = new DatagramSocket(portNumber);
            byte[] receiveBuffer = new byte[1024];

            while(true) {
                Arrays.fill(receiveBuffer, (byte)0);
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket);
                String msg = new String(receivePacket.getData());
                System.out.println("received msg: " + msg);

                ByteBuffer buffer = ByteBuffer.wrap(receiveBuffer);
                buffer.order(ByteOrder.LITTLE_ENDIAN);
                int num = buffer.getInt();
                System.out.println("Number from client: " + num);

                num += 1;
                System.out.println("Number to client: " + num);

                byte[] sendBuffer = ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(num).array();

                InetAddress address = receivePacket.getAddress();
                int port = receivePacket.getPort();
                DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, address, port);
                socket.send(sendPacket);
            }
        }
        catch(Exception e){
            e.printStackTrace();
        }
        finally {
            if (socket != null) {
                socket.close();
            }
        }
    }
}
