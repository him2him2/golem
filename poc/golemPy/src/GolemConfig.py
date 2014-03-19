import ConfigParser
import os
import shutil

GOLEM_CFG_INI_FILENAME = "golem_test_config.ini"

class DefaultConfig:

    MAIN_SECTION_STR        = "GOLEM CONFIG"
    #DEFAULT_NODE_TYPE

    DEFAULT_OPTIMAL_PEER_NUM    = 10
    DEFAULT_START_PORT          = 40102
    DEFAULT_END_PORT            = 60102
    DEFAULT_SEED_HOST           = None
    DEFAULT_SEED_HOST_PORT      = 0

    OPTIMAL_PEER_NUM_STR    = "optimal peer num"
    START_PORT_STR          = "start port"
    END_PORT_STR            = "end port"
    SEED_HOST_STR           = "seed host"
    SEED_HOST_PORT_STR      = "seed host port"

    def __init__(self, iniFile = GOLEM_CFG_INI_FILENAME):
        
        self.optimalPeerNum = DefaultConfig.DEFAULT_OPTIMAL_PEER_NUM
        self.startPort      = DefaultConfig.DEFAULT_START_PORT
        self.endPort        = DefaultConfig.DEFAULT_END_PORT
        self.seedHost       = DefaultConfig.DEFAULT_SEED_HOST
        self.seedHostPort   = DefaultConfig.DEFAULT_SEED_HOST_PORT

        print "Reading config from file {}".format( iniFile ), 

        try:
            cfg = ConfigParser.ConfigParser()
            cfg.read( iniFile )
            
            optimalPeerNum  = cfg.get( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.OPTIMAL_PEER_NUM_STR )
            startPort       = cfg.get( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.START_PORT_STR )
            endPort         = cfg.get( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.END_PORT_STR )
            seedHost        = cfg.get( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.SEED_HOST_STR )
            seedHostPort    = cfg.get( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.SEED_HOST_PORT_STR )

            self.optimalPeerNum = optimalPeerNum 
            self.startPort      = startPort      
            self.endPort        = endPort        
            self.seedHost       = seedHost       
            self.seedHostPort   = seedHostPort   

            print " ... successfully"

        except Exception as ex:
            print " ... failed with exception {}".format( ex )
            print "Trying to write default values to config file (keeping old data in bak file)"

            if os.path.isfile( iniFile ):
                shutil.copy( iniFile, iniFile + ".bak" )

            cfgfile = open( iniFile, 'w' ) #no try catch because this cannot fail (if it fails then the program shouldn't start anyway)
          
            cfg = ConfigParser.ConfigParser()

            cfg.add_section( DefaultConfig.MAIN_SECTION_STR )

            cfg.set( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.OPTIMAL_PEER_NUM_STR, self.optimalPeerNum )
            cfg.set( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.START_PORT_STR, self.startPort )
            cfg.set( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.END_PORT_STR, self.endPort )
            cfg.set( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.SEED_HOST_STR, self.seedHost )
            cfg.set( DefaultConfig.MAIN_SECTION_STR, DefaultConfig.SEED_HOST_PORT_STR, self.seedHostPort )

            cfg.write( cfgfile )
            
            cfgfile.close()
    
    def getOptimalNumberOfPeers( self ):
        return self.optimalPeerNum

    def getStartPort( self ):
        return self.startPort

    def getEndPort( self ):
        return self.endPort

    def getSeedHost( self ):
        return self.seedHost

    def getSeedHostPort( self ):
        return self.seedHostPort

    def __str__( self ):
        rs = "DefaultConfig\n"
        rs += "{:20} {self.optimalPeerNum}\n".format( "optimalPeerNumb", self = self )
        rs += "{:20} {self.startPort}\n".format( "startPort", self = self )
        rs += "{:20} {self.endPort}\n".format( "endPort", self = self )
        rs += "{:20} {self.seedHost}\n".format( "seedHost", self = self )
        rs += "{:20} {self.seedHostPort}".format( "seedHostPort", self = self )

        return rs

if __name__ == "__main__":

    cfg = DefaultConfig()
    print cfg
