# Atividade 1 - Segurança da Informação
# Equipe: Leanderson, Diego, Vinicius, Marcos e Bruno

def encrypt_rail_fence(text, key):
    # Cria uma lista de strings vazias para armazenar as letras em cada linha
    rails = [''] * key
    # Variáveis para acompanhar a direção e a posição atual
    down = False
    row = 0

    # Preenche as listas nas posições corretas
    for char in text:
        rails[row] += char
        if row == 0 or row == key - 1:
            down = not down
        if down:
            row += 1
        else:
            row -= 1

    # Junta todas as listas em uma única string
    return ''.join(rails)


def rail_fence_decipher(ciphertext, key):
    # Inicializa uma lista de listas para representar as "trilhas" vazias
    rails = [[] for _ in range(key)]

    # Inicializa variáveis para rastrear a direção e a posição das trilhas
    down = False
    row = 0

    # Preenche as trilhas com espaços vazios para garantir que a ordem seja mantida
    for i in range(len(ciphertext)):
        rails[row].append(None)
        if row == 0 or row == key - 1:
            down = not down
        row += 1 if down else -1

    # Preenche as trilhas com as letras do texto cifrado
    index = 0
    for i in range(key):
        for j in range(len(rails[i])):
            if rails[i][j] is None:
                rails[i][j] = ciphertext[index]
                index += 1

    # Recupera a mensagem decifrada lendo as letras nas trilhas na ordem correta
    plaintext = ''
    row = 0
    down = False
    for i in range(len(ciphertext)):
        plaintext += rails[row][0]
        rails[row] = rails[row][1:]
        if row == 0 or row == key - 1:
            down = not down
        row += 1 if down else -1

    return plaintext

mensagem = ("Olá, espero que vocês tenham sido capazes de decifrar este texto. Este texto faz parte da primeira atividade da "
            "disciplina de Segurança da Informação, uma disciplina optativa do curso de Sistemas de Informação do Instituto "
            "Federal de Educação, Ciência e Tecnologia do Maranhão. Porém, aqui existe um bônus: coloquei mais uma mensagem "
            "cifrada dentro dessa mesma cifra, e para decifrá-la, você precisará usar a chave 3, e não 4. Assim você conseguirá "
            "decifrar essa mensagem de forma dupla. A mensagem é a seguinte: Nu m eldoalçhmiet irae clse.aos edraume uãea ctsraam ogd  "
            "tonrsscs aEeàustsmsorouausesder g onMca smdoeddmrvd vs hda toveoc ásod tno d  erievduuufa.asrcasma!ecriolr LdoDoii ceuofnod a,"
            "od  u oslmlacna áuacdd niaemseis,fiad oa  erds ustre eemrlabihmsaeet aecrdo nunoa raua aihsdna ordr urisdsmséisetrao o eie ecrl mmi"
            " sría nia,u eor edd gad qee u ua evna seimsd cao a udd,pi e oo ssgeo ee e eeao.À ee,émlo exromséi novrvc ooa ga rfna,poeed- avraeqepd e "
            "astríe oqeqaqe atsaPrbn o eirres esgm xríi elzd eoguoB enesn ig,Vncu,Mro  rn dornaz   a,  aag to teregoS rdsa l vnnsi,qtsirmn çae,aãoir "
            "ednrfdo. o nag tupiaralqomsdonaoe.sioonts rsvsrlssz eri irel êmsupusrgodeduosm rl  lrniaépdf aneEcoaap p:ar,e ísasBo. Boa sorte!")

mensagem_oculta = ("No fundo do mar, onde a luz do sol mal alcança, há uma cidade antiga e misteriosa, feita de coral e segredos. "
                   "Suas torres de esmeralda brilham suavemente na escuridão, enquanto as criaturas marinhas dançam ao redor, guardiãs "
                   "dos mistérios enterrados nos recifes de coral. Em meio às ruínas antigas, um tesouro perdido aguarda aqueles que "
                   "ousam desvendar os enigmas do oceano. Mas cuidado, pois nem todos os segredos devem ser revelados. Às vezes, é melhor "
                   "deixar o mistério envolver você como as águas profundas, protegendo-o da verdade que pode ser mais terrível do que qualquer fantasia."
                   "Parabéns por decifrar essa mensagem! Exercício realizado pelo grupo B: Leanderson, Diego, Vinícius, Marcos e Bruno")

mensagem_grupoA = ("Ndoa naaulrt  ,ádlXnemeuilpniAnsGiat lo  dc rivmsn.ku (auseeeiarfmaaeAnn  c aqkaidrôaia csneep Aíneagnnorlaranlulspestcdntra ianaeeáEk "
                   "nraosae,iorva rsclrcposauda, lIcea oldvnneaaa çs.T,à a oara tvri osoaol cefnoF at)nalidsmnrdaselitf ebh tddr motifrootioavdcnuc "
                   "ddlbloécrnbldsy ,CiretadrsrçmumnI.ldco sxneaatads óia. a cot,neg salduotdesisrltlsooidre c  v onoo íotoxrecSah ap .r-oo eaçiliriei eik"
                   " e ,n etdioeçelo i aMur ddakge,i uo eit ei rivueB onssoiaaaci la ieg uiuieaaMnoAaoumitio. stNaEMo áropaiãoteu   eelstidldcedordtatvudega "
                   "urasemoof ien t.tesou ion Teacsaslostdesésea i rcCdht pmdg,r o ictc vonmoftAetainisssoudncddtaZb,a cooM tapnonvossce d aJe,reea lndz "
                   "nauicrcócssao nJaur bm ooecl moaalO s, e m doca veEsrtóoãeo or,l uas iagati agsned,m  dg ads nsenMvs ud  puaçeui eev l  çoa. iE ae(mã l)ao"
                   " agniisrni ornpliuneso  sqa oiiir egdreor cn ma vl a o aael zsat fd ç o,u eceánlo ã s,t ,f oa oc logAé,Sdl aotldaee   çoe see gcod m a ooc"
                   " idgn alo  oimiE  ifaSjõcs eeãlPObeee dêfelCepnvpe mtgkrobaoirodsdd.o aaanannomoao d, e l edfi màãmssi umm hi")
keyA = 6

mensagem_grupoC = ("Oe nnthniouobsa m vencidamtcosusaaee  ea ,oaems, eea auh ns nabmssçac,ei atiOddeoe soeit d nl oa s md emnreaaaa  sasodetne oottnd é tnire"
                   " lraere.Aues ed opnaauve  e rd epclelrnprumvsasedrsirole mnhs ra ets ssuts tcocr é ca.Eatsoapeadd e-aa e ea  aer znvdsr n rul   anaubd "
                   "vmenotcaplrsou,cnoasoiamep srdsli.auoe ezelzu etaarc  i ntz.sltvepolae orze gnocd svatd aj elosnn etimm clsse ual,inu eáodubt aq is otepec."
                   "Aoga tn egimjoasaiha dsadotoce msnuoi,neu ieàiar lzcmvms netad aàustsaqa.smsosqrnsaetacaev abanrara mifacataa ooeoa rmmno a ea mmop pirmgd "
                   "ueoa  mni,i e nenvh ssaoe smaamt me ter n nsasuasulsenn maq  qc r,uoaedro aenso  aun  a  niun nrmrcE tpb,o aaaar")
keyC = 4

# chave = 4
# texto_cifrado = encrypt_rail_fence(mensagem, chave)
# print("Texto cifrado:", texto_cifrado)
#
# texto_decifrado = decrypt_rail_fence(texto_cifrado, chave)
# print("Texto decifrado:", texto_decifrado)
#
# texto_cifrado2 = encrypt_rail_fence(mensagem_oculta,3)
# print("Mensagem oculta:", texto_cifrado2)
#
# texto_decifrado2 = decrypt_rail_fence(texto_cifrado2,3)
# print("Texto decifrado 2:", texto_decifrado2)

# texto_decifrado = decrypt_rail_fence(mensagem_oculta, 4)
# print("Texto decifrado:", texto_decifrado)

# Teste
print("Mensagem Teste: " + rail_fence_decipher("GsGsekfrek eoe",3))

# Decifrando as mensagens das Equipes
mensagem_decifradaA = rail_fence_decipher(mensagem_grupoA, keyA)
print("Mensagem Decifrada A: " + mensagem_decifradaA)

mensagem_decifradaC = rail_fence_decipher(mensagem_grupoC, keyC)
print("Mensagem Decifrada C: " + mensagem_decifradaC)



