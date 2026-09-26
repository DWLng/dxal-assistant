const CACHE="assistant-v3";
self.addEventListener("install",e=>{
  e.waitUntil(caches.open(CACHE).then(c=>c.addAll(["./","./anthropic.xhtml","./manifest.webmanifest","./icon-192.png","./icon-512.png"])).then(()=>self.skipWaiting()));
});
self.addEventListener("activate",e=>{
  e.waitUntil(caches.keys().then(ks=>Promise.all(ks.map(k=>{if(k!==CACHE)return caches.delete(k)})).then(()=>self.clients.claim())));
});
self.addEventListener("fetch",e=>{
  if(e.request.method!=="GET")return;
  const nav=e.request.mode==="navigate"||/text\/html/.test(e.request.headers.get("accept")||"");
  if(nav){
    e.respondWith(fetch(e.request).then(res=>{const c=res.clone();caches.open(CACHE).then(x=>x.put(e.request,c));return res;}).catch(()=>caches.match(e.request).then(x=>x||caches.match("./assistant.xhtml"))));
    return;
  }
  e.respondWith(caches.match(e.request).then(hit=>hit||fetch(e.request).then(res=>{const c=res.clone();caches.open(CACHE).then(x=>x.put(e.request,c));return res;})));
});
