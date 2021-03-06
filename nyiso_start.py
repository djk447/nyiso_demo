import requests
import datetime
import pickle
import random
from multiprocessing import Pool
from dateutil.parser import parse as dateParse



def save_obj(obj, name):
    """saves an object using pickle"""
    with open( name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    """loads an object using pickle"""
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)



def getGenerators():
    return ["59TH STREET_GT_1","74TH STREET_GT_1","74TH STREET_GT_2","ADK HUDSON___FALLS","ADK RESOURCE___RCVRY","ADK S GLENS___FALLS","ADK_NYS___DAM","AIR_PRODUCTS___DRP","ALBANY___1","ALBANY___2","ALBANY___3","ALBANY___4","ALBANY___LFGE","ALCOA_RYNLDS___DSASP","ALCOA_RYNLDS___DRP","ALLEGHENY___COGEN","ALTONA_WT_PWR","AMERICAN_REF_FUEL","AMO_HQ_IMPORTLIMIT","AMO_NPX_IMPORTLIMIT","AMO_PJM_IMPORTLIMIT","ARTHUR_KILL_2","ARTHUR_KILL_3","ARTHUR KILL_GT_1","ASHOKAN____","ASTORIA_EAST_ENERGY_CC1","ASTORIA_EAST_ENERGY_CC2","ASTORIA_GT_1","ASTORIA_GT_10","ASTORIA_GT_11","ASTORIA_GT_12","ASTORIA_GT_13","ASTORIA_GT_5","ASTORIA_GT_7","ASTORIA_GT_8","ASTORIA_GT2_1","ASTORIA_GT2_2","ASTORIA_GT2_3","ASTORIA_GT2_4","ASTORIA_GT3_1","ASTORIA_GT3_2","ASTORIA_GT3_3","ASTORIA_GT3_4","ASTORIA_GT4_1","ASTORIA_GT4_2","ASTORIA_GT4_3","ASTORIA_GT4_4","ASTORIA___2","ASTORIA___3","ASTORIA___4","ASTORIA___5","AST_ENERGY_2_CC3","AST_ENERGY_2_CC4","ATHENS_STG_1","ATHENS_STG_2","ATHENS_STG_3","ATHENS_STG_3","AUBURN___LFGE","BABYLON_RES_REC","BARRETT_IC_1","BARRETT_IC_10","BARRETT_IC_11","BARRETT_IC_12","BARRETT_IC_2","BARRETT_IC_3","BARRETT_IC_4","BARRETT_IC_5","BARRETT_IC_6","BARRETT_IC_7","BARRETT_IC_8","BARRETT_IC_9","BARRETT___1","BARRETT___2","BAYONNE___COGEN TECH 1","BAYONNE___COGEN TECH 2","BAYONNE___COGEN TECH 3","BAYONNE___COGEN TECH 4","BAYONEEC___CTG1","BAYONEEC___CTG2","BAYONEEC___CTG3","BAYONEEC___CTG4","BAYONEEC___CTG5","BAYONEEC___CTG6","BAYONEEC___CTG7","BAYONEEC___CTG8","BEACON___LESR","BEAR_SWAMP___1","BEAR_SWAMP___2","BEAVER RIVER___HYD","BEEBEE_GT_13","BERLIN___1","BETHLEHEM___GRP","BETHLEHEM___GS1","BETHLEHEM___GS2","BETHLEHEM___GS3","BETHLEHEM___STEEL","BETHPAGE_CC_5","BINGHAMTON___COGEN","BLACK RIVER___HYD","BLISS_WT_PWR","BLUE_CIRC_CHEM_DRP","BOC_GAS_DRP","BORALEX_4TH_BRANCH","BOWLINE___1","BOWLINE___2","BROOKHAVEN___DRP","BROOKLYN_NAVY_YARD","BROOKLYN___ARMY_DRP","BROOME___LFGE","BROOME_2_LFGE","BURROWS___LYONSDAL","CAITHNESS_CC_1","CALPINE_BETH_PAGE_GT_4","CALPINE_BP_GT1","CALPINE BETH_PAGE_GT4","CALSPAN___DRP","CANDIGU_WT_PWR","CARR STREET_E._SYR","CARTHAGE___PAPER","CE_NYC_DRP","CE_NYC2_DRP","CE_DUNWOOD___DRP","CE_MILLWOOD___DRP","CH_MISC_IPPS","CH_RES_NIAGARA","CH_RES_SYRACUSE","CHAFFEE___LFGE","CHATEAUG_WT_PWR","CHAUTAUQUA___LFGE","CHAT_HIGH_FALL_HYD","CH_MIDHUDSON___DRP","CH_RES_BVR_FALLS","CLINTON_WT_PWR","CLINTON___LFGE","COLONIE_LFGE__","CORNELL____","COXSACKIE___GT","CRESCENT___HYD","CRUCIBLE_METL_DRP","CSC___481_PGEN","DANC___LFGE","DANSKAMMER___1","DANSKAMMER___2","DANSKAMMER___3","DANSKAMMER___4","DANSKAMMER___DIESEL","DARTMOUTH___1","DASHVILLE___HYD","DEEP_CREEK___1","DEEP_CREEK___2","DELAWARE___LFGE","DOGLEVILLE___HYD","DOREEN____","DUNKIRK___1","DUNKIRK___2","DUNKIRK___3","DUNKIRK___4","EAST___DELAWARE_HYD","EAST HAMPTON___GT","EAST RIVER___6","EAST RIVER___7","EAST_HAMPTON___DIESEL","EAST_RIVER___1","EAST_RIVER___2","ELEC_TRO_TEK","ELLENBURG_WT_PWR","EMPIRE_CC_1","EMPIRE_CC_2","E_CANADA_CAP_HY","E_CANADA_MHWK_HY","E_FISHKILL___LBMP","ERIE_WT_PWR","FAR ROCKAWAY___4","FARRAGUT___LBMP","FENNER___WINDPWR","FIBERTEK___ENERGY","FIFEBROOK___1","FITZPATRICK____","FLUVANNA___1","FLUVANNA___2","FORT_DRUM_COGEN","FORT ORANGE____","FPL FAR_ROCK_GT1","FPL FAR_ROCK_GT2","FRANKLIN_FALL_HYD","FREEPORT_EQUS_GT1","FULTON COGEN____","FREEPORT___CT2","FULTON___LFGE","G.F.CEMENT___DRP","GARDENVILLE___LBMP","GENERAL___MILLS","GE_PLASTICS___DRP","GILBOA___1","GILBOA___2","GILBOA___3","GILBOA___4","GILBOA____","GINNA____","GLEN PARK____","GLENWOOD___4","GLENWOOD___5","GLENWOOD_IC_1_G5","GLENWOOD_IC_2_G1","GLENWOOD_IC_3_G1","GLOBAL GREEN_PORT_GT1","GLOBE___DSASP","GOETHSLN___LBMP","GOODYEAR_LAKE_HYD","GOUDEY___7","GOUDEY___8","GOWANUS_GT1_1","GOWANUS_GT1_2","GOWANUS_GT1_3","GOWANUS_GT1_4","GOWANUS_GT1_5","GOWANUS_GT1_6","GOWANUS_GT1_7","GOWANUS_GT1_8","GOWANUS_GT2_1","GOWANUS_GT2_2","GOWANUS_GT2_3","GOWANUS_GT2_4","GOWANUS_GT2_5","GOWANUS_GT2_6","GOWANUS_GT2_7","GOWANUS_GT2_8","GOWANUS_GT3_1","GOWANUS_GT3_2","GOWANUS_GT3_3","GOWANUS_GT3_4","GOWANUS_GT3_5","GOWANUS_GT3_6","GOWANUS_GT3_7","GOWANUS_GT3_8","GOWANUS_GT4_1","GOWANUS_GT4_2","GOWANUS_GT4_3","GOWANUS_GT4_4","GOWANUS_GT4_5","GOWANUS_GT4_6","GOWANUS_GT4_7","GOWANUS_GT4_8","GREENIDGE___3","GREENIDGE___4","GROVEVILLE___HYD","HAMPSHIRE___PAPER_HYD","HARDSCRABBLE_WT_PWR","HARRISBURG_CT_1","HARRISBURG_CT_2","HARRISBURG_CT_3","HARRISBURG_CT_4","HARZA MOOSE___RIVER","HEMPSTEAD____","HICKLING___1","HICKLING___2","HIGH FALLS___HY","HILLBURN___GT","HISHELDN_WT_PWR","HOLTSVILLE_IC_1","HOLTSVILLE_IC_10","HOLTSVILLE_IC_2","HOLTSVILLE_IC_3","HOLTSVILLE_IC_4","HOLTSVILLE_IC_5","HOLTSVILLE_IC_6","HOLTSVILLE_IC_7","HOLTSVILLE_IC_8","HOLTSVILLE_IC_9","HOMER CITY___01","HOMER CITY___02","HOMER CITY___03","HOPE CREEK___1","HOWARD_WT_PWR","HQ_GEN_CEDARS","HQ_GEN_CEDARS_PROXY","HQ_GEN_IMPORT","HQ_GEN_WHEEL","HQ____","HQCD____","HUDSON_AVE_10","HUDSON AVE_GT_3","HUDSON AVE_GT_4","HUDSON AVE_GT_5","HUNTER MOUNT___DRP","HUNTINGTON_RES_REC","HUNTLEY___63","HUNTLEY___64","HUNTLEY___65","HUNTLEY___66","HUNTLEY___67","HUNTLEY___68","HYLAND___LFGE","INDECK___CORINTH","INDECK___ILION","INDECK___OLEAN","INDECK___OSWEGO","INDECK___YERKES","INDIAN POINT_GT_1","INDIAN POINT_GT_2","INDIAN POINT_GT_3","INDIAN POINT___2","INDIAN POINT___3","IP___TICONDEROGA","IP CORINTH___1","ISLIP_RES_REC","JARVIS____","JENNISON___1","JENNISON___2","KEDC_GLWD_GT4","KEDC_GLWD_GT5","KEDC PORT_JEFF_GT2","KEDC PORT_JEFF_GT3","KENSICO____","KIAC_JFK_AIRPORT","KIAC_JFK_GT1","KIAC_JFK_GT2","KINTIGH____","LAKEWOOD_CT_1","LAKEWOOD_CT_2","LEDERLE____","LIEVRE RIVER____","LINDEN___1","LINDEN___2","LINDEN COGEN____","LIPA_MISC_IPP","LITTLE FALLS___HYD","LI_NEWBRDGE___DRP","LISF___SOLAR","LONG_LAKE_PHOENIX","LOVETT___3","LOVETT___4","LOVETT___5","LOWER___HUDSON","LOWER RAQUET___HYD","LWR___OSWEGATCHIE_HYD","LYONS_FALL_HYD","MADISON___COUNTY_LFGE","MAPLE_RIDGE_WT_1","MAPLE_RIDGE_WT_2","MARBLE_RIVER_WT_PWR","MARTINSCREEK___1","MARTINSCREEK___2","MARTINSCREEK___3","MARTINSCREEK___4","MERCER___1","MERCER___2","MG INDUSTRY___DRP","MID___OSWEGATCHIE_HYD","MID___RAQUETTE_HYD","MILLIKEN___1","MILLIKEN___2","MILLIKEN___DIESEL","MILLSEAT___LFGE","MODEL_CITY_ENERGY","MODERN_LFGE__","MOHAWK_PAPER___DRP","MONGAUP___HYD","MONTAUK___DIESEL","MUNSVILLE_WIND_PWR","N SALMON___HYD","N.E._GEN_SANDY PD","NARROWS_GT1_1","NARROWS_GT1_2","NARROWS_GT1_3","NARROWS_GT1_4","NARROWS_GT1_5","NARROWS_GT1_6","NARROWS_GT1_7","NARROWS_GT1_8","NARROWS_GT2_1","NARROWS_GT2_2","NARROWS_GT2_3","NARROWS_GT2_4","NARROWS_GT2_5","NARROWS_GT2_6","NARROWS_GT2_7","NARROWS_GT2_8","NEG_PENN_ALLEGHNY","NEG___GEN_MONROE","NEG CAPITAL___MECHNVIL","NEG CENTRAL_HIGH_ACRES","NEG CENTRAL___DRP","NEG CENTRAL___INDECK","NEG CENTRAL___SENECA","NEG CENTRAL___STATE_STREET","NEG MILLWOOD___DRP","NEG NORTH_FLCN_SEA","NEG NORTH_KES_CHATEGAY","NEG NORTH___ALICE_FALLS","NEG NORTH___LWR_SARANAC","NEG NORTH___PLATTSBURG","NEG WEST_LEA_LOCKPORT","NEG WEST___LANCASTR","NEPA___ENERGY","NEVERSINK___HYD","NEWARK___BAY","NEWINTON____","NEWTON___FALLS_HYD","NIAGARA____","NINE_MILE_1","NINE_MILE_2","NM_CAPITAL___DRP","NM_CENTRAL___DRP","NM_FRONTIER___DRP","NM_ST_REGIS___HYD","NORTHPORT___1","NORTHPORT___2","NORTHPORT___3","NORTHPORT___4","NORTHPORT___IC","NPX_GEN_1385_PROXY","NPX_GEN_CSC","NSINS_S._GLNS_FALLS","NUCOR_STEEL___DRP","NYISO_LBMP_REFERENCE","NYPA___ASTORIA_CC1","NYPA___ASTORIA_CC2","NYPA___HOLTSVILL","NYPA_____HELLGATE_GT1","NYPA_____HELLGATE_GT2","NYPA_BRENTWD_____GT","NYPA_GOWANUS_____GT5","NYPA_GOWANUS_____GT6","NYPA_HARLEM__RVR__GT1","NYPA_HARLEM__RVR__GT2","NYPA_KENT_____GT","NYPA_POUCH1_____GT","NYPA_VERNON_____GT2","NYPA_VERNON_____GT3","NYS_BARGE___HYD","O.H._GEN_BRUCE","OAK ORCHARD___HYD","OCC_CHEM___DRP","OLIN_CORP_DRP","OLIN_CORP_DSASP","ONEIDA_HERK_LFGE","ONONDAGA_REF_OCCRA","ONONDAGA___COGEN","ONTARIO___LFGE","ORANGEVILLE_WT_PWR","OSWEGATCHIE___HYD","OSWEGO___5","OSWEGO___6","OUTOKUMPU-AB___DRP","OXBOW____","OXY_CHEM_DSASP","PARENT_SP_ARTKLGRP","PARENT_SP_AST500","PARENT_SP_ASTGTGP2","PARENT_SP_ASTGTGRP","PARENT_SP_ASTORGRP","PARENT_SP_CAYUGGRP","PARENT_SP_DANSKGRP","PARENT_SP_GOUDEY","PARENT_SP_GOWANGRP","PARENT_SP_GOWANUS","PARENT_SP_GREENGRP","PARENT_SP_GWANSGRP","PARENT_SP_HARLMGRP","PARENT_SP_HELGTGRP","PARENT_SP_NARROGRP","PARENT_SP_RAVENSWD","PARENT_SP_ROSETON","PARENT_SP_VRNONGRP","PEEKSKILL____","PENOBSCOT___1","PGE MADISON___WINDPWR","PIERCEFIELD___HYD","PINELAWN_CC_1","PINEY___1","PINEY___2","PINEY___3","PJM_GEN_KEYSTONE","PJM_GEN_NEPTUNE_PROXY","PJM_GEN_HTP_PROXY","PJM_GEN_VFT_PROXY","PJM___ICAPUNIT","PLEASANTVLY___LBMP","POLETTI____","PONDTOOK___1","PORT_JEFF_3","PORT_JEFF_4","PORT_JEFF_IC","PPL_SHRM_GT3","PPL_SHRM_GT4","PPL PILGRIM_ST_GT1","PPL PILGRIM_ST_GT2","PROJECT___ORANGE","PROJECT___ORANGE 1","PROJECT___ORANGE 2","PYRITES___HYD","RAMAPO___LBMP","RANKINE____","RAVENSWOOD_GT_1","RAVENSWOOD_GT_10","RAVENSWOOD_GT_11","RAVENSWOOD_GT_4","RAVENSWOOD_GT_5","RAVENSWOOD_GT_6","RAVENSWOOD_GT_7","RAVENSWOOD_GT_8 TEMP GRP(8-11)","RAVENSWOOD_GT_9","RAVENSWOOD_GT2_1","RAVENSWOOD_GT2_2","RAVENSWOOD_GT2_3","RAVENSWOOD_GT2_4","RAVENSWOOD_GT3_1","RAVENSWOOD_GT3_2","RAVENSWOOD_GT3_3","RAVENSWOOD_GT3_4","RAVENSWOOD___1","RAVENSWOOD___2","RAVENSWOOD___3","RAVENSWOOD___4","RCPI_TRUST___DRP","RENSSELAER___COGEN","REVERE_CPPR_DRP","RIVERBAY____","ROCHESTER_9_IC","ROCK SPRINGS_CT_3","ROCK SPRINGS_CT_4","ROSETON___1","ROSETON___2","RUMFORD_FALL___1","RUSSELL___1","RUSSELL___2","RUSSELL___3","RUSSELL___4","RUSSELL___STATION","S SALMON___HYD","SELKIRK___II","SELKIRK___I","SENECA___ENERGY","SENECA OSWGO___HYD","SHOEMAKER___GT","SHOREHAM_IC_1","SHOREHAM_IC_2","SISSONVILLE____","SITHE_IND_GS1","SITHE_IND_GS2","SITHE_IND_GS3","SITHE_IND_GS4","SITHE___BATAVIA","SITHE___INDEPEND","SITHE___MASSENA","SITHE___OGDNSBRG","SITHE___STERLING","SOUTH CAIRO___GT","SOUTH HAMPTN___IC","SOUTHOLD___IC","ST LAWRENCE____","STATION 5_MISC_HYD","STEEL___WIND","STEUBEN_REC_LFGE","STONY___BROOK","STURGEON_POOL_HYD","SYNERGY___BIOGAS","SYRACUSE___ENERGY_ST1","SYRACUSE___ENERGY_ST2","TRIGEN___CC","SYRACUSE___POWER","UNION___PROCESSING_DRP","UPPER HUDSON___HYD","UPPER RAQUET___HYD","VISCHER___FERRY HYD","WADING RIVER_IC_1","WADING RIVER_IC_2","WADING RIVER_IC_3","WALDEN___HYDRO","WALLINGFORD___1","WALLINGFORD___2","WALLINGFORD___3","WALLINGFORD___4","WALLINGFORD___5","WARRENSBURG____","WATERSIDE___6 8 9","WDELAWARE___HYD","WEST BABYLON___IC","WEST CANADA___HYD","WESTERN_NY_WIND","WESTOVER___LESR","WETHRSFD_WT_PWR","WOODLAND____","WSPRINGFIELD___01","WSPRINGFIELD___02","WSPRINGFIELD___03","WSPRINGFIELD___10","YORK___WARBASSE"]

def getDataFromNYISO(startDate,endDate,genNum):
    generators=getGenerators()
    url = "http://dss.nyiso.com/dss_oasis/PublicReports"
    if genNum==0:
        remainingGenerators=generators[1:-1]
    elif genNum==len(generators):
        remainingGenerators=generators[0:-2]
    else:
        remainingGenerators=generators[0:genNum]+generators[genNum+1:-1]
    filter=generators[genNum]
    version='L'
    dataFormat='CSV'
    startDate=startDate.strftime("%m/%d/%Y")
    endDate=endDate.strftime("%m/%d/%Y")
    reportKey='RT_LBMP_GEN'



    payload ={'reportKey':reportKey,'remainingGenerators':remainingGenerators,'startDate':startDate,'endDate':endDate,'filter':filter,'version':version,'dataFormat':dataFormat}
    cookies=[
        "cuvon=1463080766260; cusid=1463080766257; cuvid=c15d200e48694e32b91e8d3acf0b54f1",
        "cuvon=1463027649024; cusid=1463027649021; cuvid=c824cd5329e94509965c7ddeeac787b4",
        "cuvon=1463027649024; cusid=1463027649021; cuvid=c824cd5329e94509965c7ddeeac787b4",
        "cuvon=1463080866517; cusid=1463080866514; cuvid=ca09b473dc674ec1998d8e0f84bc8e0e",
        "cuvon=1463082905896; cusid=1463082905893; cuvid=c0865a883b4345aeb7f9ffe0cf0212b3",
        "cuvon=1463082985277; cusid=1463082985275; cuvid=cdf5ce4e10584ba3a8ae57c15fa7a587",
        "cuvon=1463083068785; cusid=1463083068783; cuvid=c02e1fe6dd3944d7b6258eee1c711e2a",
        "cuvon=1463083114915; cusid=1463083114913; cuvid=c7a8b2de42b34e91a763a8fce7fb1ca9",
        "cuvon=1463083247785; cusid=1463083176572; cuvid=cd278cc4ae114c29bb4aa9e6e0f7f976"
    ]
    headers = {
        'cookie': random.choice(cookies),
        'origin': "http//www.nyiso.com",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-US,en;q=0.8",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'cache-control': "no-cache",
        'referer': "http//www.nyiso.com/public/markets_operations/market_data/custom_report/index.jsp?report=rt_lbmp_gen",
        'connection': "keep-alive"
        }



    response = requests.request("POST", url, data=payload, headers=headers)
    if response.ok:
        return response
    raise Exception('Not OK',response.reason)

def getMinDate(genName,baseURL='http://159.203.100.177:3000'):

    url = baseURL+"/generators_times"

    querystring = {"id": "eq."+genName, "select": "min_time"}

    payload = ""
    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    if len(response.json()):
        dateStr=response.json()[0].get('min_time')
        return dateParse(dateStr).date()


def postToDB(csvText, baseURL='http://159.203.100.177:3000'):
    url=baseURL+'/RT_LBMP_GEN'
    response=requests.request("POST",url,data=csvText,headers={'content-type': "text/csv"})
    if response.ok:
        return response
    raise Exception('Post Failed',response.reason)


def getDataAndPost(genNum,start=datetime.date(2016,5,11),end=datetime.date(2014,5,11)):
    failCount=0
    genName=getGenerators()[genNum]
    minDate=getMinDate(genName)
    if minDate and minDate<start:start=minDate
    print('Importing Generator '+ genName + ' Start : '+start.strftime("%m/%d/%Y"))
    endDate=start
    dateStep = datetime.timedelta(weeks=6)
    while endDate>end:
        startDate=endDate-dateStep
        message='Generator ' + genName + '('+str(genNum)+') : ' + startDate.strftime("%m/%d/%Y") + '-' + endDate.strftime("%m/%d/%Y")
        nyisoResponse=getDataFromNYISO(startDate,endDate,genNum)
        csvText = nyisoResponse.text
        if len(csvText.splitlines()) == 1:
            print('No Data For ' + message)
            failCount+=1
            if failCount>2:
                print('Lacking Data for '+ message + ' breaking')
                break

        else:
            failcount=0
            postToDB(csvText)
            print('Got Data For '+ message)
        endDate=endDate-dateStep
    print('Completed Generator '+genName)

def mapGetDataToGenNums(genNums,poolSize=6):
    pool=Pool(poolSize)
    pool.map(getDataAndPost,genNums)
    pool.close()
    print('Mapped Import Complete: '+str(genNums))

mapGetDataToGenNums(list(range(1,len(getGenerators())+1)),16)