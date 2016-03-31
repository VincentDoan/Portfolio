using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;
using System.Xml.Serialization;
using System.IO;

namespace TSI.BAE.Data
{
    /// <summary>
    /// Class containing sampleRate, duration, totalSamples, and Global.size which represents the number of channels. 
    /// It also has List of (double) calibrations, coefficients, and List (boolean) enabled, which is the enabled channels.
    /// 
    /// </summary>
    [Serializable]
    public class TestConfig
    {
        public static int ChannelCount = 10;

        /*public static string[] UUTTypes = { "MK90 Thrust Only", "MK90", "HPC Bomb" };

        public static string[] ChannelNames = { "Current",
                                                "Load channel 1 (Load cell 1)",
                                                "Load channel 2 (Load cell 2)",
                                                "Load channel 3 (Pressure transducer 1)",
                                                "Load channel 4 (Pressure transducer 2)",
                                                "Load channel 5 (spare)",
                                                "Load channel 6 (spare)",
                                                "Load channel 7 (spare)",
                                                "Load channel 8 (spare)",
                                                "Load channel 9 (HPC Bomb analog input)"
                                              };*/
        private int sampleRate;

        /// <summary>
        /// SampleRate of int value 
        /// </summary>
        public int SampleRate
        {
            get { return sampleRate; }
            set { sampleRate = value; }
        }

        private double duration;

        public double Duration
        {
            get { return duration; }
            set { duration = value; }
        }

        private double totalSamples;

        public double TotalSamples
        {
            get { return totalSamples; }
            set { totalSamples = value; }
        }

        List<double> calibrations = new List<double>(TestConfig.ChannelCount);

        public List<double> Calibrations
        {
            get { return calibrations; }
            set { calibrations = value; }
        }

        TransducerSettings trasducerSetting;

        public TransducerSettings TrasducerSetting
        {
            get { return trasducerSetting; }
            set { trasducerSetting = value; }
        }

        //List<bool> enabled = new List<bool>(Global.size);

       /* public List<bool> Enabled
        {
            get { return enabled; }
            set { enabled = value; }
        }*/

        double clockrate;

        public double Clockrate
        {
            get { return Clockrate; }
            set { Clockrate = value; }
        }

        long bufferSize;

        public long BufferSize
        {
            get { return BufferSize; }
            set { BufferSize = value; }
        }

        public TestConfig()
        {
            Name = "Test 1";
            IgnitionPulseCurrent = 0.25;
            IgnitionPulseDuration = 500;
            UUTResMax = 100;
            UUTResMin = 80;
            sampleRate = 5000;
            duration = 1.2;
            totalSamples = sampleRate * duration;
            UUTType = "MK90 Thrust Only";

            //TransSettings = new List<TransducerSettings>();

        }

       /* public TestConfig(string name, double ignitionPulseCurrent, int ignitionPulseDuration, int uutResMin, int uutResMax, int sampleRate, double duration, string uutType, List<double> calibrations, int channelCount, List<TransducerSettings> transSettings)
        {
            this.Name = name;
            this.IgnitionPulseCurrent = ignitionPulseCurrent;
            this.IgnitionPulseDuration = ignitionPulseDuration;
            this.UUTType = uutType;
            this.UUTResMax = uutResMax;
            this.UUTResMin = uutResMin;
            this.UUTType = "MK90 Thrust Only";
            this.sampleRate = sampleRate;
            this.duration = duration;
            this.totalSamples = sampleRate * duration;
            this.calibrations = calibrations;
            ChannelCount = channelCount;
            this.TransSettings = transSettings;
        }*/

 



        public string Name { get; set; }
        public double IgnitionPulseCurrent { get; set; }
        public double IgnitionPulseDuration { get; set; }
        public double UUTResMin { get; set; }
        public double UUTResMax { get; set; }
        public string UUTType { get; set; }
        public List<TransducerSettings> TransSettings { get; set; }

        /// <summary>
        /// Static function that serializes a DataAcquisitionConfiguration object to XML. 
        /// </summary>
        /// <param name="fileName"></param>
        /// <param name="dac"></param>
        /*public static void Serialize(string fileName, TestConfig config)
        {
            
            if (fileName.Substring(fileName.Length - 4) == ".xml")
            {
                Console.WriteLine("Serialized.");
       
                XmlSerializer serializer = new XmlSerializer(typeof(TestConfig));
                using (TextWriter textWriter = new StreamWriter(fileName))
                {
                    serializer.Serialize(textWriter, config);
                    textWriter.Close();
                }
            }
        }*/

        public static void Serialize(string fileName, UUTInformation uut)
        {
            Console.WriteLine("Serialized.");

            XmlSerializer serializer = new XmlSerializer(typeof(TestConfig));
            using (TextWriter textWriter = new StreamWriter(fileName))
            {
                serializer.Serialize(textWriter, uut);
                textWriter.Close();
            }
        }

        /// <summary>
        /// Static function that Deserializes a XML file to a DataAcquistionConfiguration object.
        /// </summary>
        /// <param name="fileName"></param>
        /// <returns></returns>

        public static TestConfig Deserialize(string fileName)
        {

            //Check if fileName exists
            XmlSerializer mySerializer = new XmlSerializer(typeof(TestConfig));
            // To read the file, create a FileStream.
            FileStream myFileStream = new FileStream(fileName, FileMode.Open);
            // Call the Deserialize method and cast to the object type.
            TestConfig config = new TestConfig();
            config = (TestConfig)mySerializer.Deserialize(myFileStream);

            myFileStream.Close();
            return config;
        }
    }

}
