using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TSI.BAE.Data
{
    /// <summary>
    /// A class containg all of the UUtInformation including testTime, motorName, and serialNo
    /// </summary>
    public class UUTInformation
    {
        DateTime testTime = DateTime.Now;

        public DateTime TestTime
        {
            get { return testTime; }
            set { testTime = value; }
        }
        string motorName;

        public string MotorName
        {
            get { return motorName; }
            set { motorName = value; }
        }
        string serialNo;

        public string SerialNo
        {
            get { return serialNo; }
            set { serialNo = value; }
        }

        string temperature = "Cold";

        public string Temperature
        {
            get { return temperature; }
            set { temperature = value; }
        }

        public UUTInformation()
        {

        }

        public UUTInformation(DateTime testTime, string motorName, string serialNo)
        {
            this.testTime = testTime;
            this.motorName = motorName;
            this.serialNo = serialNo;
        }

        public UUTInformation(string motorName, string serialNo)
        {
            this.motorName = motorName;
            this.serialNo = serialNo;
        }

        public UUTInformation(DateTime testTime, string motorName, string serialNo, string temperature)
        {
            this.testTime = testTime;
            this.motorName = motorName;
            this.serialNo = serialNo;
            if (temperature == "Hot")
            {
                this.temperature = temperature;
            }

        }
    }
}
