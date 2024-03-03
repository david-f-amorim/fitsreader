(David Amorim, 2019)

                        DESCRIPTION: 
    This program transforms the data of a '.fits'-file 
    into an Aitoff projection in galactical coordinates 
    and saves the resulting image as a '.png'-file. 
       
-----------------------------------------------------------
FURTHER INFORMATION:
-----------------------------------------------------------
    DATA INPUT:
        All information is to be entered into files called
        'input.csv' and 'sources.csv' located in the same 
        directory as this program.
    
    REQUIRED MODULES:
        This program requires numpy, astropy, pandas and matplotlib.
        To install any of those modules enter a variation of 
        this command into the Terminal:
            'python3 -m pip install example_module'
        
    REQUIRED VERSION OF PYTHON:
        This program was written in python3 and might behave
        differently for an older version of python. 
        Make sure to use the 'python3' command when running the 
        programme.
        
    ACCEPTED FILES:
        This programme is designed for '.fits'-files with a 
        format of 180x360 rows and columns. 
        The programme might work differently or not at all for 
        other formats.
        When entering the path to the '.fits'-file make sure to 
        give the complete path ('/home/user/.../file.fits')
        
    COORDINATE TRANSFORMATION:
        This programme expects the input data to be in a cartesian
        coordinate system with the point [0,0] in the top left corner.
        This coordinate grid is then transformed and reordered to fit
        the astronomical conventions of the aitoff projection and x-axis
        labelling.
        Inserting data into the programme that does not match the 
        aforementioned specifications will result in jumbled output.
            
    DESIGN OF PLOT:
        The plot's design is mainly dependent on the lines 89-96:
            To change the background colour tweak the command 
                'fig.patch.set_facecolor()'
            To change the coordinate grid tweak the command 
                'ax.grid()'
            To change the labelling of the x-axis tweak the command 
                'plt.xticks()'
            To change the title tweak the command 
                'plt.title()'
        
    ADDING POINTS TO PLOT:
        To add coloured markers or text on certain points of the plot
        enter the information into a file called 'sources.csv' located 
        in the same directory as this programme.
        An overview of accepted colours can be found here: 
            'https://i.stack.imgur.com/lFZum.png'
        An overview of accepted symbols can be found here:
            'https://matplotlib.org/3.1.1/api/markers_api.html'
        
    OUTPUT FILE:
        This programme saves the resulting image as a '.png'-file
        within the same directory the programme itself is located in.
-----------------------------------------------------------
