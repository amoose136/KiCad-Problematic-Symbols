import glob
baddies = []
bannedPinNames= ['VSSA','VSS','VS','VPP','VMEM','VEE','Vdrive','VDDF','VDDA','VDD','VDC','VD','VCOM','VCCQ','VCC','VBUS','VAC','VAA','PRI_MID','PRI_LO','PRI_HI','NEUT','LINE','HT','GNDS','GNDREF','GNDPWR','GNDD','GNDA','GND','Earth_Protective','Earth_Clean','AC','-VSW','-VDC','-BATT','-48V','-36V','-24V','-15V','-12VA','-12V','-10V','-9VA','-9V','-8V','-6V','-5VA','-5V','-3V3','-2V5','+VSW','+VDC','+BATT','+48V','+36V','+28V','+24V','+15V','+12VA','+12V','+12P','+12LF','+12L','+12C','+10V','+9VA','+9V','+8V','+7.5V','+6V','+5VP','+5VL','+5VD','+5VA','+5V','+5P','+5F','+5C','+4V','+3V8','+3V3','+3V0','+3.3VP','+3.3VDAC','+3.3VADC','+3.3VA','+3.3V','+2V8','+2V5','+1V35','+1V8','+1V5','+1V2','+1V1','+1V0']
kicadLibrariesDirectory = 'C:\Program Files\KiCad\share\kicad\library\\'
libraries = glob.glob(kicadLibrariesDirectory+"*.lib")
for libraryPath in libraries:
    currentLibraryName = libraryPath.split('\\')[-1] # get end of path
    with open(libraryPath) as f:
        library_text_lines = f.readlines()
        currentSymbolName = ''
        for line in library_text_lines:
            if "DEF" in line.split():
                currentSymbolName = line.split()[1] # the second word is the symbol name
            words = line.split()
            currentWorkingSymbol=currentLibraryName + '\\' + currentSymbolName
            if words[0] == "X" and words[1] in bannedPinNames and currentWorkingSymbol not in baddies:
                baddies.append(currentWorkingSymbol)
with open('problematic_symbols.txt', 'w') as f:
    for line in baddies:
        f.write(line)
        f.write('\n')
