#!/bin/bash

PWD="/home/yp11/Desktop/genomes/hg38/chromFa_tagger"

#for our data that doesn't have Ref or NC..
#input 1: #sample
#input 2: #hap
#input 3: species(default:Homo sapiens)
#input 4: has Y? (default:Y)

samplen=${1:-default}
   hapn=${2:-1}
species=${3:-Homosapiens}
  haveY=${4:-Y}

#determine if the input has chromosome Y
if [ "$haveY" == 'Y' ]; then
 Filename=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y M)
else
 Filename=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X M)
fi

cd $PWD

name=${samplen}'_'${hapn}'_all_chr.fa'
  
echo -n >  $name

i=0

for x in "${Filename[@]}"
do
 i=$((i + 1))

#the file to be change
 ofile='chr'$x'.fa'

#change the header and combine into a huge file with the listed order
 ref_position='>gi|0000000'$i'|chr'$x':NC_000000.'$i'|'$species

 sed -i "1s/.*/$ref_position/" $ofile
 
#gi|000000000|chrI:NC_000000.1|c elegans ce10 WS220

 cat $ofile >> $name

done


#useit  % compile the hg19 genome using tagscan
#system('..\genwin -a ../hg19_idx.txt -o ../hg19_out.bin hg19_all_chr.fa');
#system('..\sortGWI -o ../hg19_idx.bin -u ../hg19_out.bin');

#% test use of it
#system('..\fetchGWI -a ../hg19_idx.txt -i ../hg19_idx.bin -m 2 CCTGTCGTCCTTGAAGAA');

#return
