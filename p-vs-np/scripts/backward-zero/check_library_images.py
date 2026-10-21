"""Check every fixed-library record is its claimed literal image."""
import gzip
import json
from pathlib import Path
import endpoints as ep

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
OUT=HERE/'output'

def literal_record(row):
    row=dict(row)
    for field in ('goal','f'):
        if field in row:
            row[field]=ep.c.serialize(ep.image(ep.c.parse(row[field],'native')[0]))
    if 'format' in row:
        row['format']='not-or'
    if 'subs' in row:
        row['subs']={key:ep.c.serialize(ep.image(ep.c.parse(value,'native')[0]))
                     for key,value in row['subs'].items()}
    return row

def main():
    path=OUT/'library-images-194.json'
    cert={'complete':False,'failures':[],'laws':[]}
    def save():
        path.write_text(json.dumps(cert,indent=2)+'\n')
    save()
    try:
        checked=json.loads((OUT/'certificate-194.json').read_text())['library']
        for name in ep.fixed():
            source=ROOT/checked[name]['native']['path']
            image=ROOT/checked[name]['not-or']['path']
            records=0
            with gzip.open(source,'rt') as sf, gzip.open(image,'rt') as tf:
                while True:
                    a,b=sf.readline(),tf.readline()
                    if not a and not b:
                        break
                    if not a or not b or literal_record(json.loads(a))!=json.loads(b):
                        raise AssertionError(name+' literal-image mismatch at record '+str(records-1))
                    records+=1
            if records-1!=checked[name]['native']['lines']:
                raise AssertionError(name+' line count mismatch')
            cert['laws'].append({'name':name,'lines':records-1,'full_record_image_match':True,
                                 'native':str(source.relative_to(ROOT)),
                                 'image':str(image.relative_to(ROOT))})
        cert['complete']=True
        save()
        print('All',len(cert['laws']),'full fixed-library pairs match literal images;',path.relative_to(ROOT))
    except Exception as err:
        cert['failures'].append({'type':type(err).__name__,'message':str(err)})
        save()
        raise

if __name__=='__main__':
    main()
