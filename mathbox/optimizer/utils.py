from mathbox.calculus.differential import diff

def local_minmax(signal, closed=False):
    threshold = (max(signal) - min(signal)) * 0.001 # avoid floating point errors
    max_pos = []
    min_pos = []
    diff_x = diff(signal)
    gradient = [x if abs(x) > threshold else 0.0 for x in diff_x]
    
    if closed == True:
        if gradient[0] > 0:
            min_pos.append(0)
        elif gradient[0] < 0:
            max_pos.append(0)
        else:
            for i in range(1, len(gradient)):
                if gradient[i] < 0:
                    max_pos.extend(range(0, i + 1))
                    break
                elif gradient[i] > 0:
                    min_pos.extend(range(0, i + 1))
                    break
                else:
                    continue

    for i in range(len(gradient) - 1):
        if gradient[i] > 0 and gradient[i + 1] < 0:
            max_pos.append(i + 1)
            continue
        if gradient[i] < 0 and gradient[i + 1] > 0:
            min_pos.append(i + 1)
            continue
        # > < or < > continue
        if gradient[i] == 0:
            continue
        if gradient[i] > 0 and gradient[i + 1] == 0:
            for j in range(i + 1, len(gradient)):
                if gradient[j] < 0:
                    max_pos.extend(range(i + 1, j + 1))
                    break
                if gradient[j] == 0:
                    continue
                if gradient[j] > 0:
                    break
        if gradient[i] < 0 and gradient[i + 1] == 0:
            for j in range(i + 1, len(gradient)):
                if gradient[j] > 0:
                    min_pos.extend(range(i + 1, j + 1))
                    break
                if gradient[j] == 0:
                    continue
                if gradient[j] < 0:
                    break

    if closed == True:
        if gradient[-1] < 0:
            min_pos.append(len(gradient))
        elif gradient[-1] > 0:
            max_pos.append(len(gradient))
        else:
            for i in range(len(gradient) - 1, 0, -1):
                if gradient[i] > 0:
                    max_pos.extend(range(len(gradient), i, -1))
                    break
                elif gradient[i] < 0:
                    min_pos.extend(range(len(gradient), i, -1))
                    break
                else:
                    continue
    
    max_points = [(i,x) for i,x in enumerate(signal) if i in max_pos]
    min_points = [(i,x) for i,x in enumerate(signal) if i in min_pos]
    return max_points, min_points

def argmax(alist):
    # np.argmax output the 1st, this output the last
    return max((x,i) for i,x in enumerate(alist))[1]